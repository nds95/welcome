#피타고라스 방정식을 이용한 문제 풀이
#조건 1 : a < b < c
#조건 2 : a + b + c = 1000
#조건이 만족했을 때 a * b * c 값 구하기

for a in range(1, 1000):            # a값을 1부터 999까지 반복실행
    for b in range(1, 1000):        # b값을 1부터 999까지 반복실행
        c = 1000 - a - b            # 1000 = a + b + c라는 것을 이용해서 'c = 1000 - a - b'로 변경
        if a*a + b*b == c*c and a < b < c:      # 비교연산자 조건을 기입하여 필터링
            print(a * b * c)