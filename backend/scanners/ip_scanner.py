import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ABUSEIPDB_KEY")


def scan_ip(ip):
    url = "https://api.abuseipdb.com/api/v2/check"

    headers = {
        "Key": API_KEY,
        "Accept": "application/json"
    }

    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)

        if response.status_code != 200:
            return {
                "type": "ip_scan",
                "target": ip,
                "status": "error",
                "indicators": {},
                "message": "IP scan failed. API returned an error."
            }

        data = response.json()

        if "data" not in data:
            return {
                "type": "ip_scan",
                "target": ip,
                "status": "error",
                "indicators": {},
                "message": "IP scan failed. Unexpected API response."
            }

        info = data["data"]

        abuse_score = info.get("abuseConfidenceScore", 0)
        reports = info.get("totalReports", 0)
        country = info.get("countryCode", "Unknown")
        isp = info.get("isp", "Unknown")

        if abuse_score == 0:
            risk = "Safe"
        elif abuse_score < 50:
            risk = "Suspicious"
        else:
            risk = "High Risk"

        message = f"""
IP Scan Result

IP Address: {ip}
Country: {country}
ISP: {isp}

Abuse Score: {abuse_score}
Reports: {reports}

Status: {risk}
"""

        return {
            "type": "ip_scan",
            "target": ip,
            "status": "success",
            "raw": data,
            "indicators": {
                "abuse_score": abuse_score,
                "reports": reports,
                "country": country,
                "isp": isp
            },
            "message": message
        }

    except Exception as e:
        return {
            "type": "ip_scan",
            "target": ip,
            "status": "error",
            "indicators": {},
            "message": f"IP scan failed: {str(e)}"
        }