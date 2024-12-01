# 200 for *답안 확인

# 날짜 리스트
# 시가(open), 고가 (high), 저가 (low) , 종가(close) 
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

# 수익 
# 초기화
num = 0

# 1번째 인덱스부터 슬라이싱
for list in ohlc[1:]:

    # 3번째 요소 - 0번째 요소 = 수익  
    num += (list[3] - list[0])
print(num)

# 결과 :
# 0 