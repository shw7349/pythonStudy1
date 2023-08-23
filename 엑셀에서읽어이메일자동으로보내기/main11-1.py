import openpyxl

# 설치 pip install openpyxl
# 엑셀 파일 열기

wb = openpyxl.load_workbook('python\엑셀에서읽어이메일자동으로보내기\이메일.xlsx')
sheet = wb.active

# 각 행의 이메일과 이름 출력

for row in sheet.iter_rows(min_row=2, values_only=True): # 첫 번째 행은 제외
    email, name = row
    print(f"{email}, {name}")
    
# 엑셀 파일 닫기
wb.close()
