# 293 file CSV 파일 쓰기 *답안 확인

# 매수종목.csv 생성
# csv 모듈 
import csv

# 파일 열기
# 경로와 쓰기/텍스트 모드
f = open("C:/Users/황서영/Desktop/매수종목.csv", "wt")


# csv 파일에 객체 전달
write = csv.writer(f)

# 텍스트 쓰기
write.writerow(['종목명', '종목코드', 'PER'])
write.writerow(['삼성전자', '005930', '15.79'])
write.writerow(['NAVER', '035420', '55.82'])

# 파일 닫기
f.close()

# 결과 :
# PS C:\Users\황서영\Desktop\python_study> & C:/Users/황서영/AppData/Local/Programs/Python/Python313/python.exe c:/Users/황서영/Desktop/python_study/12_exception/291_300_file/293_file.py
# 종목명	종목코드	PER
		
# 삼성전자	5930	15.79
		
# NAVER	35420	55.82


