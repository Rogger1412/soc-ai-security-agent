from agent.intent_parser import detect_intent
from agent.target_extractor import extract_target
from agent.planner import create_plan
from agent.tool_executor import execute_plan
from agent.response_builder import build_response
from agent.memory import save_context, get_context
from utils.logger import logger


def handle_query(message: str):
    try:
        message = message.strip()

        if not message:
            return {
                "message": "Please enter a command or investigation request."
            }

        logger.info(f"Received user message: {message}")

        # ---------------------------
        # Step 1: Detect intent
        # ---------------------------
        intent = detect_intent(message)
        logger.info(f"Detected intent: {intent}")

        # ---------------------------
        # Step 2: Extract target
        # ---------------------------
        target = extract_target(message, intent)
        logger.info(f"Extracted target: {target}")

        # ---------------------------
        # Step 3: Help / fallback mode
        # ---------------------------
        if intent == "help":
            ctx = get_context()

            return {
                "message": f"""
SOC AI Security Agent

Supported commands:

• 8.8.8.8
• https://example.com
• port scan 127.0.0.1
• investigate 8.8.8.8
• I clicked this link https://example.com
• paste a SHA256 hash

Last Target: {ctx.get("last_target")}
Last Intent: {ctx.get("last_intent")}
"""
            }

        # ---------------------------
        # Step 4: Validate target
        # ---------------------------
        intents_requiring_target = {
            "ip_scan",
            "url_scan",
            "hash_scan",
            "port_scan",
            "investigation",
            "incident_response"
        }

        if intent in intents_requiring_target and not target:
            return {
                "message": f"""
Target Extraction Failed

Intent detected: {intent}

I could not identify a valid target in your request.

Examples:
• 8.8.8.8
• https://example.com
• port scan 127.0.0.1
• investigate 8.8.8.8
"""
            }

        # ---------------------------
        # Step 5: Build execution plan
        # ---------------------------
        plan = create_plan(intent, target)
        logger.info(f"Execution plan: {plan}")

        if not plan:
            return {
                "message": f"""
Planning Failed

Intent: {intent}
Target: {target if target else 'N/A'}

No valid execution plan could be created for this request.
"""
            }

        # ---------------------------
        # Step 6: Execute tools
        # ---------------------------
        results = execute_plan(plan, target)
        logger.info(f"Execution results keys: {list(results.keys())}")

        # ---------------------------
        # Step 7: Build final response
        # ---------------------------
        response = build_response(intent, target, results)

        # ---------------------------
        # Step 8: Save memory/context
        # ---------------------------
        save_context(intent=intent, target=target, result=response)
        logger.info("Context saved successfully")

        return response

    except Exception as e:
        logger.exception("Agent orchestration error")
        return {
            "message": f"Agent error: {str(e)}"
        }