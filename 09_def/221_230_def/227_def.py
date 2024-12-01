# 227 def *답안 확인

# 함수 정의
# 매개변수 정의
def printmxn(str227, nums):
    # 문자 길이 / 숫자
    lens = int(len(str227)/nums)
    # 마지막 인덱스까지 가져오기 위함
    for a in range(lens+1):
        # 매개변수[시작:마지막]
        # 슬라이싱
        print(str227[a*nums : a * nums+nums])

printmxn("아이엠어보이유알어걸", 3)

# 결과 :
# 아이엠
# 어보이
# 유알어
# 걸