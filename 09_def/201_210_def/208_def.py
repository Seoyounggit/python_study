# 208 def 

print("A") # A
def message1() : # 첫번째 함수 
    print("B")
print("C") # C
def message2() : # 두번째 함수 
    print("D")
message1() # B
print("E") # E
message2() # D

# 예상 결과 :
# A
# C 
# B //첫번째 함수
# E 
# D //두번째 함수

# 결과 :
# A
# C
# B
# E
# D