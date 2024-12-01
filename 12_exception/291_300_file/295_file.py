# 295 file 파일 읽기2

# 파일 열기
# 경로와 읽기 모드
f = open('C:/Users/황서영/Desktop/매수종목2.txt', 'r')

# 텍스트 읽기
reads = f.read()
# 텍스트 호출
print(reads)

# 파일 닫기
f.close()

# 결과 :
# PS C:\Users\황서영\Desktop\python_study> & C:/Users/황서영/AppData/Local/Programs/Python/Python313/python.exe c:/Users/황서영/Desktop/python_study/12_exception/291_300_file/295_file.py
# 종목명,종목코드,PER

# 삼성전자,005930,15.79

# NAVER,035420,55.82

