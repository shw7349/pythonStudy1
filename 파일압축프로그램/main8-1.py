import zipfile
# 설치 : pip install pyzipper

def compress_file(file_path):
    with zipfile.ZipFile(file_path + '.zip','w') as zip_file:
            zip_file.write(file_path)
            
if __name__ == '__main__':
    compress_file('파일압축프로그램\압축.txt')