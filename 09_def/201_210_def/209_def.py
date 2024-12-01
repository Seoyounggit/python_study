# 209 def

def message1(): # 첫번쨰 함수
    print("A")

def message2(): # 두번째 함수
    print("B") 
    message1() # 첫번째 함수 호출 문자 포함 

message2() # B 
# A

# 예상 결과 :
# B //두번째 함수 
# A // 두번째 함수에 포함한 첫번째 함수 

# 결과 :
# B
# A