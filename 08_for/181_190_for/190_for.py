# 190 for

# 호수 리스트
apart = [ [101, 102], [201, 202], [301, 302] ]

 # row 변수에 리스트 저장    
for row in apart:
        # [101, 102]
        print(row)
        # col 변수에 요소 하나씩 할당
        for col in row:
            # 101 호
            # 102 호
            # 한라인당 하나씩 출력
            print(col, "호")
print("-" * 5)

# 결과 :
# 101 호
# 102 호
# 201 호
# 202 호
# 301 호
# 302 호
# -----