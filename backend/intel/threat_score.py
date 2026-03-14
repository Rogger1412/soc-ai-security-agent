def calculate_threat_score(result):
    if not isinstance(result, dict):
        return 0, "LOW"

    result_type = result.get("type", "")
    indicators = result.get("indicators", {})

    score = 0

    if result_type == "ip_scan":
        abuse_score = indicators.get("abuse_score", 0)
        reports = indicators.get("reports", 0)

        score += min(abuse_score, 60)

        if reports >= 20:
            score += 20
        elif reports >= 5:
            score += 10
        elif reports > 0:
            score += 5

    elif result_type == "url_scan":
        malicious = indicators.get("malicious", 0)
        suspicious = indicators.get("suspicious", 0)

        score += malicious * 18
        score += suspicious * 10

    elif result_type == "hash_scan":
        malicious = indicators.get("malicious", 0)
        suspicious = indicators.get("suspicious", 0)

        score += malicious * 20
        score += suspicious * 8

    elif result_type == "port_scan":
        open_ports = indicators.get("open_ports", [])

        risky_ports = {
            21: 10,
            23: 25,
            25: 10,
            139: 10,
            445: 20,
            3306: 10,
            3389: 20
        }

        for entry in open_ports:
            port = entry.get("port")
            if port in risky_ports:
                score += risky_ports[port]

    if score > 100:
        score = 100

    if score >= 70:
        severity = "HIGH"
    elif score >= 35:
        severity = "MEDIUM"
    else:
        severity = "LOW"

    return score, severity