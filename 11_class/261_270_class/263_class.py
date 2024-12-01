# 263 class 메서드 1 *답안 확인

# 클래스 정의
class Stock:
    # 생성자 정의
    def __init__(self, name, code):
        self.name = name
        self.code = code

    # 메서드 추가
    def set_name(self, name):
        self.name = name 

# 객체 정의
# 초기화 
a = Stock(None, None)

# 메서드 호출
a.set_name("삼성전자")
# 속성 출력
print(a.name)

# 결과 : 삼성전자