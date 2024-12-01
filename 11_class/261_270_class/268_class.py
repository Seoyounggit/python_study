# 268 class 메서드 추가

# 클래스 정의 
class Stock:
    # 생성자 정의
    # 종목명, 종목코드, PER, PBR, 배당수익률 생성자
    def __init__(self, name, code, per, pbr,dividend ):
        self.name = name
        self.code = code 
        self.per = per
        self.pbr = pbr 
        self.dividend = dividend
    
    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code
    
    # PER 메서드 추가 
    def set_per(self, per):
        self.per = per
    
    # PBR 메서드 추가
    def set_pbr(self, pbr):
        self.pbr = pbr     

    # 배달수익률 메서드 추가
    def set_dividend(self, dividend):
        self.dividend = dividend


    def get_name(self):
        return self.name

    def get_code(self):
        return self.code