import requests
# 외부IP 출력하기1
# IP 주소 가져오기

response = requests.get('https://api.ipifiy.org')
external_ip = response.text
print("외부 IP: " + external_ip)