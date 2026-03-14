import ipaddress


def create_plan(intent: str, target: str = None):

    # Basic scans
    if intent == "ip_scan":
        return ["scan_ip"]

    if intent == "url_scan":
        return ["scan_url"]

    if intent == "hash_scan":
        return ["scan_hash"]

    if intent == "port_scan":
        return ["scan_ports"]

    # Device / remediation
    if intent == "device_scan":
        return ["scan_device"]

    if intent == "threat_removal":
        return ["remove_threat"]

    # Incident response
    if intent == "incident_response":
        return ["scan_url", "resolve_domain", "scan_ip", "incident_guidance"]

    # Investigation mode
    if intent == "investigation":

        if target:
            # If target is an IP
            try:
                ip_obj = ipaddress.ip_address(target)

                # Private/internal IP
                if ip_obj.is_private:
                    return ["scan_ports", "containment_guidance"]

                # Public IP
                return ["scan_ip", "scan_ports"]

            except ValueError:
                pass

            # If target looks like a URL or domain
            if target.startswith("http") or "." in target:
                return ["scan_url", "resolve_domain", "scan_ip", "scan_ports"]

        # Fallback
        return ["scan_ip"]

    # Default
    return []