# 214 def

# 숫자, 숫자
def fun(a, b) :
    print(a + b) 

# 문자, 숫자
fun("안녕", 3) # 문자와 숫자는 더하기 불가능
# 에러 발생

# 결과 : 
#     print(a + b)
#           ~~^~~
# TypeError: can only concatenate str (not "int") to str

# 올바른 작성
# fun("안녕","안녕") //str+str
# fun(1,2) //int+int
# fun(1,int(1)) //int+int 형변환 
# fun("안녕", str(1)) //str+str 형변환