import os
import hashlib
import requests
from ai_helper import explain_threat

API_KEY = "7b31bf347cf7bed3f3922be134caec018e7c1801a7c61f7392d646fdba36e469"


def get_file_hash(file_path):
    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)

        return sha256.hexdigest()

    except:
        return None


def check_hash(hash_value):

    url = f"https://www.virustotal.com/api/v3/files/{hash_value}"

    headers = {
        "x-apikey": API_KEY
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            return None

        data = response.json()

        stats = data["data"]["attributes"]["last_analysis_stats"]

        return stats

    except:
        return None


def scan_device(folder="C:\\"):

    infected_files = []

    for root, dirs, files in os.walk(folder):

        for file in files:

            path = os.path.join(root, file)

            file_hash = get_file_hash(path)

            if not file_hash:
                continue

            result = check_hash(file_hash)

            if not result:
                continue

            if result["malicious"] > 0:

                # AI explanation
                ai_analysis = explain_threat(
                    f"A suspicious file located at {path} was detected as malicious by {result['malicious']} antivirus engines."
                )

                infected_files.append({
                    "file": path,
                    "malicious": result["malicious"],
                    "ai_analysis": ai_analysis
                })

    if not infected_files:
        return {
            "type": "device_scan",
            "message": """
Device Scan Result

Status: ✅ No known malicious files detected.

Recommendations:
• Keep antivirus updated
• Avoid downloading cracked software
• Regularly update your operating system
"""
        }

    message = "\nDevice Scan Result\n\n⚠️ Threats Detected\n\n"

    for f in infected_files:

        message += f"""
Threat File: {f['file']}
Detection Count: {f['malicious']}

AI Security Analysis:
{f['ai_analysis']}

"""

    message += """
Recommended Actions

1. Delete the suspicious file
2. Run a full antivirus scan
3. Disconnect internet if suspicious behavior continues
4. Update system security patches

To remove a file using this tool type:

delete C:\\path\\to\\file.exe
"""

    return {
        "type": "device_scan",
        "message": message
    }


def delete_threat(file_path):

    try:

        if os.path.exists(file_path):

            os.remove(file_path)

            return {
                "type": "delete",
                "message": f"""
Threat Removal Result

File removed successfully.

Removed File:
{file_path}

Recommendations
• Run a full system scan
• Restart your system
• Update antivirus definitions
"""
            }

        else:

            return {
                "type": "delete",
                "message": "File not found. It may already be removed."
            }

    except Exception as e:

        return {
            "type": "delete",
            "message": f"Error removing file: {str(e)}"
        }