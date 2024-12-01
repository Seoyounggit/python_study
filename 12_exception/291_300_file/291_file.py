# 12. 파이썬 입출력과 예외 처리
# 파이썬으로 컴퓨터에 저장된 파일 읽거나 쓰기 가능함.
# 프로그램 작성때 발생하는 예외를 사전에 미리 잘 처리하는 것이 중요함

# 291~300

# 290 file 파일 쓰기1

# 매수종목1.txt 생성 
# 파일 열기 
# 파일 경로와 쓰기 모드
f = open("C:/Users/황서영/Desktop/매수종목1.txt", 'w')

# 파일에 텍스트 쓰기 
f.write('005930')
f.write('\n005380')
f.write('\n035420')

# 파일 닫기
f.close()

# 결과 :
#  PS C:\Users\황서영\Desktop\python_study> & C:/Users/황서영/AppData/Local/Programs/Python/Python313/python.exe c:/Users/황서영/Desktop/python_study/12_exception/291_file.py
# 005930
# 005380
# 035420