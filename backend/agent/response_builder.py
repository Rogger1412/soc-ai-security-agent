from intel.threat_score import calculate_threat_score
from intel.ai_explainer import explain
from database.db import cursor, conn
from datetime import datetime


def build_response(intent, target, results):
    scan_sections = []
    guidance_sections = []

    overall_score = 0
    overall_severity = "LOW"

    for _, result in results.items():

        if not isinstance(result, dict):
            continue

        result_type = result.get("type", "")

        # ---------------- DOMAIN RESOLUTION ----------------
        if result_type == "domain_resolution":
            if "ip" in result:
                message = f"""
Domain Resolution

Domain: {result.get("domain", "Unknown")}
Resolved IP: {result.get("ip", "Unknown")}
"""
                scan_sections.append(message.strip())

            elif "error" in result:
                scan_sections.append(
                    f"Domain Resolution Failed\n\nReason: {result.get('error')}"
                )

            continue

        # ---------------- GUIDANCE / REMEDIATION ----------------
        if result_type in ["guidance", "remediation", "device_scan"]:
            if "message" in result:
                guidance_sections.append(result["message"].strip())
            continue

        # ---------------- REAL SCAN RESULTS ----------------
        score, severity = calculate_threat_score(result)
        overall_score = max(overall_score, score)

        if severity == "HIGH":
            overall_severity = "HIGH"
        elif severity == "MEDIUM" and overall_severity != "HIGH":
            overall_severity = "MEDIUM"

        if "message" in result and result["message"]:
            scan_sections.append(result["message"].strip())

        explanation = explain(result)
        if explanation:
            scan_sections.append(f"Analysis:\n{explanation}")

    # ---------------- BUILD BODY TEXT ----------------
    body_parts = []

    if scan_sections:
        body_parts.append("\n\n".join(scan_sections))

    if guidance_sections:
        body_parts.append("\n\n".join(guidance_sections))

    body_text = "\n\n".join(body_parts).strip()

    if not body_text:
        body_text = "No detailed investigation output was generated."

    # ---------------- FINAL MESSAGE ----------------
    final_message = f"""
SOC Investigation Result

Intent: {intent}
Target: {target if target else 'N/A'}

Threat Score: {overall_score}
Severity: {overall_severity}

{body_text}
""".strip()

    # ---------------- SAVE INVESTIGATION TO DATABASE ----------------
    try:
        lines = [line.strip() for line in body_text.split("\n") if line.strip()]
        summary_line = lines[0][:200] if lines else "Investigation completed"

        cursor.execute(
            """
            INSERT INTO investigations (timestamp, target, intent, severity, score, summary)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                datetime.now().isoformat(),
                str(target) if target is not None else "N/A",
                str(intent),
                str(overall_severity),
                int(overall_score),
                str(summary_line),
            ),
        )

        conn.commit()
        print("Investigation saved to DB")

    except Exception as e:
        print("Database logging failed:", e)

    return {
        "message": final_message
    }