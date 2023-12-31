from googletrans import Translator

# install : pip install googletrans==4.0.0-rc1

# 번역할 파일 경로

input_file_path = "python\영어문서를한글로자동번역\영어문서.txt"

# 번역된 파일 저장 경로

output_file_path = "python\영어문서를한글로자동번역\한글번역.txt"


# 번역기 생성

translator = Translator()

# 파일 읽기

with open(input_file_path, "r" , encoding="utf-8") as input_file:
    text = input_file.read()
    
# 번역

result = translator.translate(text, dest="ko")

# 번역된 결과를 파일에 쓰기

with open(output_file_path, "w", encoding="utf-8") as output_file:
    output_file.write(result.text)