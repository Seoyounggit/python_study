# 180 for *답안 확인

# 5일 간의 리스트
# 저가
low_prices  = [100, 200, 400, 800, 1000]
# 고가
high_prices = [150, 300, 430, 880, 1000]

# 변등폭
volatility = []

# 리스트 요소의 갯수 
for a in range(len(low_prices)):
    # 변등폭 값 = 고가 요소 - 저가 요소
    volatility.append(high_prices[a] - low_prices[a])
    # 결과값 출력
    print(volatility)

# 결과 :
# [50]
# [50, 100]
# [50, 100, 30]
# [50, 100, 30, 80]
# [50, 100, 30, 80, 0]   