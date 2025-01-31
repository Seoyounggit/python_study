# 226 def *답안 확인

# 함수 정의
# 매개변수 정의
def print_5xn(str226):
    # 숫자 형변환 후
    # 문자열을 5개의 한덩어리로 나눔
    lens = int(len(str226)/5)

    # 마지막1번째 인덱스까지 가져오기 위한 덧셈
    # 0번째 인덱스 : 아이엠어보
    # 1번째 인덱스 : 이유알어걸
    for a in range(lens+1):
        # 시작 인덱스, 마지막 인덱스(포함x)
        # 슬라이싱
        print(str226[a*5: a*5+5])

print_5xn("아이엠어보이유알어걸")

# 결과 :
# 아이엠어보
# 이유알어걸