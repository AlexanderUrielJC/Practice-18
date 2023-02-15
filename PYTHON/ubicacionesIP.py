import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print("Dirección IP:", ip_address)