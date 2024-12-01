# 219 def

# 함수 정의
# 매개변수 정의
def print_sum(a, b):
    # 매개변수 호출
    # 파라미터 값들
    print(a+b) #합
    print(a-b) #차
    print(a*b) #곱
    print(a/b) #나눗셈

# 입력 받은 데이터 1, 2
num1 = input("첫번째 숫자: ") # a
num2 = input("두번째 숫자: ") # b

# 합/차/곱/나눗셈
# 결과값
print_sum(int(num1), int(num2))

# 결과 : 
# 첫번째 숫자: 3
# 두번째 숫자: 3
# 6 #3+3    //합
# 0 #3-3    //차
# 9 #3*3    //곱
# 1.0 #3/3  //나눗셈