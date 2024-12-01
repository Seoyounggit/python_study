# 199 for *답안 확인

# 날짜 리스트
# 시가(open), 고가 (high), 저가 (low) , 종가(close) 
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

# 1번째부터 인덱싱
for list in ohlc[1:]:
    # 종가 > 고가에서
    if list[3] > list[0]: 
        # 이후, 고가 - 저가 = 변등폭 인 경우
        print(list[1]-list[2])

# 결과 :
# 10