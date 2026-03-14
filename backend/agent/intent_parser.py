import re


def detect_intent(message: str) -> str:
    msg = message.lower().strip()

    # Port scan
    if msg.startswith("port scan"):
        return "port_scan"

    # Device scan
    if "scan my device" in msg or "scan device" in msg or "scan my system" in msg:
        return "device_scan"

    # Threat removal
    if msg.startswith("delete ") or msg.startswith("remove "):
        return "threat_removal"

    # Incident response
    if "clicked" in msg and "link" in msg:
        return "incident_response"

    # Investigation mode
    if "investigate" in msg or "analyze" in msg:
        return "investigation"

    # URL scan
    if re.search(r"https?://[^\s]+", msg):
        return "url_scan"

    # SHA256 hash scan
    if re.search(r"\b[a-fA-F0-9]{64}\b", msg):
        return "hash_scan"

    # IP scan
    if re.search(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", msg):
        return "ip_scan"

    return "help"