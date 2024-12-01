# 198 for

# 날짜 리스트
# 시가(open), 고가 (high), 저가 (low) , 종가(close) 
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

# 변등폭 = 고가와 저가의 차이
# 고가 - 저가 = 변등폭  
# 변등폭 리스트
# 초기화
volatility = []

# 1번째 요소부터 슬라이싱
for list in ohlc[1:]:
   
   # 1번째 고가 - 2번째 저가 = 변등폭 
   # 리스트 요소에 하나씩 추가
   volatility.append(list[1] - list[2])

# 결과 값   
print(volatility)

# 결과 :
# [40, 30, 10]