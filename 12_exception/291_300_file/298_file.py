# 298 file 특정 예외만 처리
# *답안 확인

# 입력 값
try: 
    a = 5/0 # 0으로 나누기 

# 특정한 경우만 
# 예외 처리
except ZeroDivisionError:
    print('0으로 나누기 실패!')

# 결과 : 0으로 나누기 실패!
