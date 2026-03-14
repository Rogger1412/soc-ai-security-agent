import requests
import os
from dotenv import load_dotenv

load_dotenv()

VT_API_KEY = os.getenv("VIRUSTOTAL_KEY")


def scan_hash(file_hash):
    try:
        url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
        headers = {"x-apikey": VT_API_KEY}

        r = requests.get(url, headers=headers, timeout=10)

        if r.status_code != 200:
            return {
                "type": "hash_scan",
                "target": file_hash,
                "status": "error",
                "indicators": {},
                "message": "Hash not found in VirusTotal."
            }

        data = r.json()
        stats = data["data"]["attributes"]["last_analysis_stats"]
        malicious = stats.get("malicious", 0)
        suspicious = stats.get("suspicious", 0)

        message = f"""
Hash Scan Result

SHA256: {file_hash}

Malicious Detections: {malicious}
Suspicious Detections: {suspicious}
"""

        return {
            "type": "hash_scan",
            "target": file_hash,
            "status": "success",
            "raw": data,
            "indicators": {
                "malicious": malicious,
                "suspicious": suspicious
            },
            "message": message
        }

    except Exception as e:
        return {
            "type": "hash_scan",
            "target": file_hash,
            "status": "error",
            "indicators": {},
            "message": f"Hash scan failed: {str(e)}"
        }