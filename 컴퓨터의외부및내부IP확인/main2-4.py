import socket
import requests

# 내부IP, 외부IP 한 번에 출력하기
hostname = socket.gethostname()
internal_ip = socket.gethostbyname(hostname)

# 외부IP rkwudhrl
response = requests.get('https://ipinfo.io/ip')
external_ip = response.text.strip()

# 출력
print("내부 IP:", internal_ip)
print("외부 IP:", external_ip)