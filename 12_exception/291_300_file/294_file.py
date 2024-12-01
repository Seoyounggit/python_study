# 294 file 파일 읽기1

# 파일 열기
# 파일 경로와 읽기 모드
f = open("C:/Users/황서영/Desktop/매수종목1.txt", "r")

# 파일 안에 저장된 텍스트 읽기
reads = f.read()
# 텍스트 출력
print(reads) 

# 파일 닫기
f.close()

# 결과 :
# PS C:\Users\황서영\Desktop\python_study> & C:/Users/황서영/AppData/Local/Programs/Python/Python313/python.exe c:/Users/황서영/Desktop/python_study/12_exception/291_300_file/294_file.py
# 005930
# 005380
# 035420
