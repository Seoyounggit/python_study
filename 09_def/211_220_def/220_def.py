# 220 def *답안 확인

# 함수 정의
# 매개변수 정의
def print_max(a, b, c):

    # 최곳값 초기화
    max_num = 0 
    # a라는 변수로 초기화 
    max_num = a

    # b가 a보다 큰 경우 
    if b > max_num:
        max_num = b 
    
    # c가 b보다 큰 경우 
    if c > max_num:
        max_num = c 
    
    # 최곳값
    # 결과값
    print(max_num)

# 입력 받은 데이터 1,2,3
num1 = int(input("첫번째: "))
num2 = int(input("두번째: "))
num3 = int(input("세번째: "))

# 입력받은 값 a,b,c를 매개변수 num1,num2,num3로 
# 함수에 재정의    
print_max(num1, num2, num3)