from scanners.ip_scanner import scan_ip
from scanners.url_scanner import scan_url
from scanners.hash_scanner import scan_hash
from scanners.port_scanner import scan_ports
from tools.domain_resolver import resolve_domain


def execute_plan(plan, target=None):
    results = {}
    current_target = target

    for step in plan:

        if step == "scan_ip":
            results["ip_scan"] = scan_ip(current_target)

        elif step == "scan_url":
            results["url_scan"] = scan_url(current_target)

        elif step == "scan_hash":
            results["hash_scan"] = scan_hash(current_target)

        elif step == "scan_ports":
            results["port_scan"] = scan_ports(current_target)

        elif step == "resolve_domain":
            domain_data = resolve_domain(current_target)
            results["domain_resolution"] = domain_data

            if isinstance(domain_data, dict) and "ip" in domain_data:
                current_target = domain_data["ip"]

        elif step == "scan_device":
            results["device_scan"] = {
                "type": "device_scan",
                "target": current_target,
                "status": "success",
                "indicators": {},
                "message": """
Device Scan Result

Real full local antivirus scanning is not yet integrated.

Current limitation:
• This agent can investigate IPs, URLs, hashes, and open ports
• Full device malware scanning requires Defender / ClamAV / YARA integration

Recommendation:
• Integrate Windows Defender CLI or ClamAV next
• Use YARA rules for suspicious file detection
"""
            }

        elif step == "remove_threat":
            results["remove_threat"] = {
                "type": "remediation",
                "target": current_target,
                "status": "success",
                "indicators": {},
                "message": """
Threat Removal Guidance

Automatic deletion is not yet fully wired.

Recommended actions:
• Isolate the suspicious file
• Delete it manually if confirmed malicious
• Run a full antivirus scan
• Review recent downloads and startup items
"""
            }

        elif step == "incident_guidance":
            results["incident_guidance"] = {
                "type": "guidance",
                "target": current_target,
                "status": "success",
                "indicators": {},
                "message": """
Incident Response Guidance

• Do not open the link again
• Run a full device scan
• Change passwords if credentials were entered
• Enable MFA
• Review browser extensions and downloads
• Monitor for suspicious logins
"""
            }

        elif step == "containment_guidance":
            results["containment_guidance"] = {
                "type": "guidance",
                "target": current_target,
                "status": "success",
                "indicators": {},
                "message": """
Containment Guidance

• Restrict exposure to risky services
• Review firewall rules
• Disable unused services
• Investigate authentication logs
"""
            }

    return results