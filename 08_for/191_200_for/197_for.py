# 197 for

# 날짜 리스트
# 시가(open), 고가 (high), 저가 (low) , 종가(close) 
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

# 리스트 1번째 요소부터 슬라이싱
for list in ohlc[1:]:
    # 3번째 요소 종가 >= 1번째 요소 시가
    if list[3] >= list[0]:
        
        # 결과값 
        print(list[3])

# 결과 :
# 100
# 310       