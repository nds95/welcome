revenue_month = 0           #월 매출 값을 저장 할 수 있는 변수 정의
revenue_list = []           #매출 리스트를 저장 할 수 있는 변수 정의
with open('chicken.txt', 'r') as f:     #chicken.txt에 있는 내용을 읽기 전용으로 불러와 f변수라는 이름으로 정의한다.
    for line in f:                      #f인덱스 수 만큼 line변수 이름으로 순서대로 갖고오기
        data = line.strip().split(": ") #data변수로 한 줄씩 화이트 스페이스 없이 ": "기준으로 갖고오기  * ": "는 없어진다.
        revenue = int(data[1])          #revenue에 각 줄마다 1번 인덱스에 있는 값을 정수로 갖고오기
        revenue_month += revenue        #revenue_month에 해당 금액들을 계속 더하기

        #리스트 길이 구하기
        len_list = line.strip().split(": ")     #len_list 변수로 한 줄씩 화이트 스페이스 없이 ": "기준으로 갖고오기  * ": "는 없어진다.
        revenue_list += len_list                #revenue_list에 len_list를 더해 revenue_list를 완성시킨다.

print(revenue_month / (len(revenue_list) / 2))  #월 매출 / (revenue_list길이) / 2)   * revenue_list 길이 / 2 = 해당 월 일수다.