# 179 for

# 종가 데이터 리스트
my_list = [100, 200, 400, 800, 1000, 1300]

# 3일 이동 평균 계산
# 4번 반복
for a in range(4):
    # 3가지 요소/3
    # 요소당 한칸씩 이동(3개)/3 = 평균
    print((my_list[a]+my_list[a+1]+my_list[a+2])/3)
    
# 결과 :
# 233.33333333333334
# 466.6666666666667
# 733.3333333333334
# 1033.3333333333333    
