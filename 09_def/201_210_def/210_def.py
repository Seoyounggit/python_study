# 210 def * 답안 확인

def message1(): # 첫번째 함수
    print("A")

def message2(): # 두번째 함수
    print("B")

def message3(): # 세번째 함수 * 3
    for i in range (3) :
        message2() # B
        print("C")
    message1() # A //세번째 함수 반복 이후 (들어쓰기)

message3() # B
# C
# A

# 예상 결과 :
# B
# C
# B
# C
# B
# C // 세번째 함수 *3
# A // 그다음 첫번째 함수

# 결과 : 
# B
# C
# B
# C
# B
# C
# A