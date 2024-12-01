# 240 def 

def fun0(num) :
    return num * 2

def fun1(num) :
    return fun0(num + 2)

def fun2(num) :
    num = num + 10
    return fun1(num)

c = fun2(2) # 2+10=12 +2=14 *2=28
print(c) # 28
# 예상 결과 : 28

# 결과 : 28