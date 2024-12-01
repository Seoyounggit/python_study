# 239 def

def fun1(num) :
    return num + 4

def fun2(num) :
    num = num + 2
    return fun1(num)

c = fun2(10) # 10+2=12 + 4 = 16 //fun2 + fun1
print(c) # 16
# 예상 결과 : 16
#  결과 : 16 