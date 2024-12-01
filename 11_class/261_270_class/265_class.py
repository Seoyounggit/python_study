# 265 class 메서드 3

# 클래스 정의 
class Stock:
    # 생성자 정의 
    def __init__(self, name, code):
        self.name = name 
        self.code = code

    # 메서드 추가
    # 종목명
    def set_naem(self, name):
        self.name = name

    # 종목코드
    def set_code(self, code):
        self.code = code

    # 종목명 업데이트
    def get_name(self):
        return self.name
    
    # 종목코드 업데이트
    def get_code(self):
        return self.code

# 객체 정의
samsung  = Stock('삼성전자', '005980')
# 속성 호출
print(samsung.name)
print(samsung.code)

# 업데이트 속성 호출
print(samsung.get_name())
print(samsung.get_code())

# 결과 :
# 삼성전자
# 005980
# 삼성전자
# 005980