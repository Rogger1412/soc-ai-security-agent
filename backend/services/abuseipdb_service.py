from dotenv import load_dotenv
import requests
import os
from utils.logger import logger
load_dotenv()
ABUSEIPDB_KEY = os.getenv("ABUSEIPDB_KEY")


def check_ip(ip):

    url = "https://api.abuseipdb.com/api/v2/check"

    headers = {
        "Key": ABUSEIPDB_KEY,
        "Accept": "application/json"
    }

    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }

    try:

        response = requests.get(url, headers=headers, params=params)

        if response.status_code != 200:
            logger.error("AbuseIPDB request failed")
            return None

        return response.json()

    except Exception as e:
        logger.error(f"AbuseIPDB error: {e}")
        return None