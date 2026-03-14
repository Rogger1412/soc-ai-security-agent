from dotenv import load_dotenv
import requests
import base64
import os
from utils.logger import logger
load_dotenv()
VT_API_KEY = os.getenv("VIRUSTOTAL_KEY")


def get_url_report(url):

    try:
        url_bytes = url.encode("utf-8")
        url_id = base64.urlsafe_b64encode(url_bytes).decode().strip("=")

        vt_url = f"https://www.virustotal.com/api/v3/urls/{url_id}"

        headers = {
            "x-apikey": VT_API_KEY
        }

        r = requests.get(vt_url, headers=headers, timeout=10)

        if r.status_code != 200:
            logger.error(f"VirusTotal URL lookup failed: {url}")
            return None

        return r.json()

    except Exception as e:
        logger.error(f"VirusTotal error for {url}: {e}")
        return None