# 196 for

# 날짜 리스트
# 시가(open), 고가 (high), 저가 (low) , 종가(close) 
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

# 리스트 중 1번째부터 슬라이싱
for close in ohlc[1:]:

   # 종가(close) > 150 큰 경우
   # 3번째 요소만 인덱싱 후 비교
    if close[3] > 150:
        # 결과 값
        print(close[3])

# 결과 :
# 190
# 310