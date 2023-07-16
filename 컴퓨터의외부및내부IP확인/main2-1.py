import socket
# 내부IP 출력하기1
# 호스트 이름 가져오기
hostname = socket.gethostname()

# IP 주소 가져오기
ip_address = socket.gethostbyname(hostname)
print("내부 IP: " + ip_address)