import requests
from bs4 import BeautifulSoup
import re

# install : pip install beautifulsoup4

url = "https://v.daum.net/v/20230303140011566" # 이메일을 수집할 웹 페이지 주소
response = requests.get(url) # 웹 페이지 요청
soup = BeautifulSoup(response.text, "html.parser") # BeautifulSoup 객체 생성
emails = []

# 이메일 패턴
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-z|a-z]{2,}\b'

# 웹 페이지에서 모든 테스트 추출
text = soup.get_text()


# 이메일 패턴 매칭 후 리스트에 추가
for match in re.findall(email_pattern, text):
    emails.append(match)
    
# 중복제거
emails = list(set(emails))

# 결과 출력
print(emails)