# 297 file 예외처리 및 리스트에 저장
# * 답안 확인

# PER 리스트
per = ["10.31", "", "8.00"]

# 예외 처리용 
# 리스트 초기화 
lists = []

# 입력 값
for i in per:
    try: # 실수 형변환
        num = float(i)
    
    # 예외 처리
    except: 
        # 0으로 초기화
        num = 0 
        # 리스트에 저장
        # 한요소로 분리 
        lists.append(num)

# 결과 출력
print(num)

# 결과 : 8.0