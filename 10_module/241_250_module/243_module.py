# 243 module *답안 확인

# 모듈 호출 
import datetime

# now 변수에 현재 시간 저장
now = datetime.datetime.now()

# 오늘로부터 5일, 4일, 3일, 2일, 1일 전의 날짜
# 5일 -1로 하루 뒤로 씩
# => 5,4,3,2,1로 
for day in range(5, 0, -1):
    # 날짜 할당
    delta = datetime.timedelta(days=day)
    # 현재 날짜 - n일
    date = now - delta
    # 결과 값
    print(date)

# 결과 :
# 2024-11-26 17:15:45.354032
# 2024-11-27 17:15:45.354032
# 2024-11-28 17:15:45.354032
# 2024-11-29 17:15:45.354032
# 2024-11-30 17:15:45.354032