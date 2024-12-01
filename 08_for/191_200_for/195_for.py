# 195 for

# 날짜 리스트
# 시가(open), 고가 (high), 저가 (low) , 종가(close) 
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

# 종가 리스트만 출력 
# 1번째 요소부터 슬라이싱

for close in ohlc[1:]:
    # [100, 110, 70, 100]
    # print(close)
    # 3번째 요소만 인덱싱
    print(close[3])

# 결과 :
# 100
# 190
# 310