import requests
from utils.logger import logger


def get_ip_location(ip):

    url = f"http://ip-api.com/json/{ip}"

    try:
        r = requests.get(url, timeout=5)

        if r.status_code != 200:
            logger.error(f"GeoIP request failed for {ip}")
            return None

        data = r.json()

        return {
            "country": data.get("country"),
            "city": data.get("city"),
            "region": data.get("regionName"),
            "isp": data.get("isp"),
            "lat": data.get("lat"),
            "lon": data.get("lon")
        }

    except Exception as e:
        logger.error(f"GeoIP error for {ip}: {e}")
        return None