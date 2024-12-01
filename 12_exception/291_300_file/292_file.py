# 292 file 파일 쓰기2

# 매수종목2.txt 생성 
# 파일 열기
# 경로와 쓰기 모드
f = open("C:/Users/황서영/Desktop/매수종목2.txt", "w")

# 텍스트 쓰기
f.write('005930 삼성전자')
f.write('\n005380 현대차')
f.write('\n035420 NAVER')

# 파일 닫기
f.close()

# 결과 :
# PS C:\Users\황서영\Desktop\python_study> & C:/Users/황서영/AppData/Local/Programs/Python/Python313/python.exe c:/Users/황서영/Desktop/python_study/12_exception/292_file.py
# 005930 삼성전자
# 005380 현대차
# 035420 NAVER