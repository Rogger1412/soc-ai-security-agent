def explain(result):
    if not isinstance(result, dict):
        return "No valid scan result available."

    result_type = result.get("type", "")
    indicators = result.get("indicators", {})

    if result_type == "ip_scan":
        abuse_score = indicators.get("abuse_score", 0)
        reports = indicators.get("reports", 0)
        country = indicators.get("country", "Unknown")
        isp = indicators.get("isp", "Unknown")

        if abuse_score == 0:
            return f"This IP appears clean with no abuse reports. Provider: {isp}, Country: {country}."

        if abuse_score < 50:
            return f"This IP shows moderate abuse history with {reports} reports and should be monitored."

        return f"This IP has a strong abuse profile with {reports} reports and should be treated as potentially malicious."

    if result_type == "url_scan":
        malicious = indicators.get("malicious", 0)
        suspicious = indicators.get("suspicious", 0)

        if malicious == 0 and suspicious == 0:
            return "This URL currently appears clean in available threat intelligence feeds."

        if malicious > 0:
            return "This URL is flagged as malicious and may host malware or phishing content."

        return "This URL is suspicious and should not be trusted without deeper investigation."

    if result_type == "hash_scan":
        malicious = indicators.get("malicious", 0)

        if malicious == 0:
            return "This hash has no malicious detections in the current intelligence source."

        return "This hash is associated with malware or suspicious software and should not be executed."

    if result_type == "port_scan":
        open_ports = indicators.get("open_ports", [])

        if not open_ports:
            return "No high-value common ports were exposed in this scan."

        services = ", ".join([f"{x['port']} ({x['service']})" for x in open_ports])
        return f"Open services detected: {services}. Review whether these services should be publicly or internally exposed."

    return "No threat explanation available."