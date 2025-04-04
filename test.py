import socket

def check_connectivity(ip_range):
    """
    Verifica a conectividade com um intervalo de endereços IP.
    """
    for ip in ip_range:
        try:
            # Tenta criar um socket para o endereço IP na porta 80 (HTTP)
            socket.setdefaulttimeout(1)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((ip, 80))
            print(f"Conectividade detectada com {ip}")
        except (socket.timeout, socket.error):
            print(f"Não foi possível conectar a {ip}")

if __name__ == "__main__":
    ip_range = ["8.8.8.8", "1.1.1.1", "8.8.4.4"]  # Exemplo de intervalo de IPs
    check_connectivity(ip_range)