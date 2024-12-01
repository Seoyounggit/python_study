# 235 def *답안 확인

# 함수 정의
# 매개 변수 정의
def convert_int (str235) :
    # 숫자 형변환 후, ','와 '' 기준으로 분할
    return int(str235.replace(',', ''))

# 파라미터 값 호출
str235 = convert_int("1,234,567")
# 결과 출력
print(str235)
# 결과 : 1234567