import socket
from utils.logger import logger

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP-Alt"
}


def scan_ports(host, timeout=1):
    open_ports = []

    try:
        for port, service in COMMON_PORTS.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))
            sock.close()

            if result == 0:
                open_ports.append({"port": port, "service": service})

        if open_ports:
            lines = "\n".join([f"{x['port']} ({x['service']})" for x in open_ports])
        else:
            lines = "No common open ports detected."

        message = f"""
Port Scan Result

Target: {host}

{lines}
"""

        return {
            "type": "port_scan",
            "target": host,
            "status": "success",
            "raw": {"open_ports": open_ports},
            "indicators": {
                "open_ports": open_ports,
                "open_port_count": len(open_ports)
            },
            "message": message
        }

    except Exception as e:
        logger.error(f"Port scan failed for {host}: {e}")
        return {
            "type": "port_scan",
            "target": host,
            "status": "error",
            "indicators": {},
            "message": f"Port scan failed: {str(e)}"
        }