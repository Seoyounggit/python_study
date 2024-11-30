# 123 if *답안 확인

# 나라별 돈 딕셔너리 
# 단위:금액
money = {'달러':1167, 
         '엔':1.069, 
         '유료':1268, 
         '위안':171}

# 입력받은 값
# str
users = input("입력: ")

# 공백() 기준으로 분할 후 두 변수에 값 할당
num, currency = users.split()

# 환전 = 입력 값 * 환율 = 원
# num : float로 형변환 
# currency : 입력 값(단위)은 money에서 key로 value값 호출(float)
print(float(num) * money[currency], "원")

# 결과 : 
# 입력: 1000 달러
# 1167000.0 원
