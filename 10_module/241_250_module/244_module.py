# 244 module 현재 시간만 출력

# 모듈 가져오기
import datetime
# now 변수에 모듈 할당 
now =  datetime.datetime.now()
# 2024-12-01 17:27:49.339524
# print(now)
# strftime 메서드로 포맷 후 시간만 출력
print(now.strftime("%H:%M:%S"))

# 결과 :
# # 17:18:53