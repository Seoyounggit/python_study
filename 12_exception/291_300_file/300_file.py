# 300 file try, except, else, finally 구조 

# PER 리스트 
per = ["10.31", "", "8.00"]

# 입력 값
for i in per:
    # 수행 코드
    try:
        print(float(per))  

    # 예외 처리
    except : # per = 0 
        print(0) # 296번 참고

    # 예외 발생x
    else:
        print('정상 작동')

    # 예외와 무관,
    # 항상 수행 중
    finally:
        print('항상 수행 중')

# 결과 :
# 0
# 항상 수행 중 
# 0
# 항상 수행 중 
# 0
# 항상 수행 중 