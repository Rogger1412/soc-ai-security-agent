import socket

def resolve_domain(url):

    try:

        domain = url.replace("https://","").replace("http://","").split("/")[0]

        ip = socket.gethostbyname(domain)

        return {
            "type": "domain_resolution",
            "domain": domain,
            "ip": ip
        }

    except Exception as e:

        return {
            "type": "domain_resolution",
            "error": str(e)
        }