# 267 class 객체 생성

# 클래스 정의 
class Stock:
    # 생성자 정의
    # 종목명, 종목코드, PER, PBR, 배당수익률 생성자
    def __init__(self, name, code, per, pbr, money):
        self.name = name
        self.code = code 
        self.per = per
        self.pbr = pbr 
        self.money = money
    
    # 종목명 메서드 추가
    def set_name(self, name):
        self.name = name

    # 종목코드 메서드 추가 
    def set_code(self, code):
        self.code = code
    
    # 종목명 속성 업데이트 
    def get_name(self):
        return self.name
    
    # 종목코드 속성 업데이트
    def get_code(self):
        return self.code

# 객체 생성    
samsung = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
# 속성 호출
print(samsung.name, samsung.code, samsung.per, samsung.pbr, samsung.money)
# 결과 : 삼성전자 005930 15.79 1.33 2.83