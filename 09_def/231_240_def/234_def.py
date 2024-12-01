# 234 def

# 함수 정의
# 매개변수 정의
def pickup_even(ints):
    # 리스트 초기화 
    lists = []
    # a 변수에 리스트 저장
    for a in ints:
        # 2의 배수인 짝수만 출력
        if a % 2 == 0:
            # 한요소씩 리스트에 저장
            lists.append(a)
    # 결과값 출력    
    print(lists)
    # 리스트로 반환
    return lists
            

# 매개변수 정의
pickup_even([3, 4, 5, 6, 7, 8])

# 결과 : [4, 6, 8]