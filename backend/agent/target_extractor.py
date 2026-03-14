import re

IP_PATTERN = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
HASH_PATTERN = r"\b[a-fA-F0-9]{64}\b"
URL_PATTERN = r"https?://[^\s]+"


def extract_target(message: str, intent: str):
    message = message.strip()

    # URL-based intents
    if intent in ["url_scan", "incident_response"]:
        url_match = re.search(URL_PATTERN, message)
        if url_match:
            return url_match.group()

    # Hash-based intent
    if intent == "hash_scan":
        hash_match = re.search(HASH_PATTERN, message)
        if hash_match:
            return hash_match.group()

    # IP-based intents
    if intent in ["ip_scan", "investigation", "port_scan"]:
        ip_match = re.search(IP_PATTERN, message)
        if ip_match:
            return ip_match.group()

    # Threat removal may carry a file path or target later
    if intent == "threat_removal":
        return message

    return None