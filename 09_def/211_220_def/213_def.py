# 213 def

def fun(str213) :
    print(str213)

fun() # 매개변수 값 할당X 
# 함수만 호출하여 에러 발생   

# 결과 : 
#     fun()
#     ~~~^^
# TypeError: fun() missing 1 required positional argument: 'str213'

# 올바른 작성
# fun("hi")