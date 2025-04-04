import socket

def resolve_dns(ip_range):
    results = []
    for ip in ip_range:
        try:
            hostname = socket.gethostbyaddr(ip)[0]
            results.append((ip, hostname))
        except socket.herror:
            results.append((ip, None))
    return results