# 264 class 메서드 2

# 클래스 정의 
class Stock:
    # 생성자 정의 
    def __init__(self, name, code):
        self.name = name 
        self.code = code

    # 메서드 추가
    def set_code(self, code):
        self.code = code

# 객체 정의
# None로 초기화
a = Stock(None, None)

# 메서드 호출 
a.set_code("005930")
# 속성 출력
print(a.code)     

# 결과 : 005930