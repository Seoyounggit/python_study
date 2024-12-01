# 245 module 문자 시간타입으로 변환 *답안 확인

# 모듈 가져오기
import datetime

# 시간 지정
day = "2024-05-04"
# 문자열을 시간 타입으로 변환 
strp = datetime.datetime.strptime(day, "%Y-%m-%d")
# 출력 값
print(strp)
# 타입 확인용
print(type(strp))

# 결과 :
# 2024-05-04 00:00:00
# <class 'datetime.datetime'>