from services.virustotal_service import get_url_report
from utils.logger import logger


def scan_url(url):
    try:
        report = get_url_report(url)

        if not report or "data" not in report:
            return {
                "type": "url_scan",
                "target": url,
                "status": "error",
                "indicators": {},
                "message": f"""
URL Scan Result

URL: {url}

Status: Unable to retrieve VirusTotal data
"""
            }

        stats = report["data"]["attributes"]["last_analysis_stats"]

        malicious = stats.get("malicious", 0)
        suspicious = stats.get("suspicious", 0)
        harmless = stats.get("harmless", 0)
        undetected = stats.get("undetected", 0)

        if malicious > 0:
            risk = "Dangerous"
        elif suspicious > 0:
            risk = "Suspicious"
        else:
            risk = "Safe"

        message = f"""
URL Scan Result

URL: {url}

Risk Level: {risk}

Malicious Engines : {malicious}
Suspicious Engines: {suspicious}
Harmless Engines  : {harmless}
Undetected        : {undetected}
"""

        logger.info(f"URL scanned: {url}")

        return {
            "type": "url_scan",
            "target": url,
            "status": "success",
            "raw": report,
            "indicators": {
                "malicious": malicious,
                "suspicious": suspicious,
                "harmless": harmless,
                "undetected": undetected
            },
            "message": message
        }

    except Exception as e:
        logger.error(f"URL scan failed for {url}: {e}")
        return {
            "type": "url_scan",
            "target": url,
            "status": "error",
            "indicators": {},
            "message": f"URL scan failed: {str(e)}"
        }