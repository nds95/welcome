#투표된 숫자 구하기

votes = ['김영자', '강승기', '최만수', '김영자', '강승기', '강승기', '최만수', '김영자', '최만수', '김영자',
         '최만수', '김영자', '김영자', '최만수', '최만수', '최만수', '강승기', '강승기', '김영자', '김영자', '최만수', '김영자', '김영자',
         '강승기', '김영자']          #투표 리스트 작성

# 카운트 한 투표결과를 'vote_counter'라는 변수값으로 class 'dict' 정의
vote_counter = {}

a = 0
b = 0
c = 0
for name in votes:      #for문을 이용, 변수로 'name' 설정, 리스트 'votes'의 인덱스 갖고오기
    if name == '김영자':       # if문 활용, 인덱스 내용이 '김영자'일 때
        a += 1      # a = a + 1
    elif name == '강승기':     # if문 활용, 인덱스 내용이 '강승기'일 때
        b += 1
    elif name == '최만수':     # if문 활용, 인덱스 내용이 '최만수'일 때
        c += 1
    vote_counter['김영자'], vote_counter['강승기'], vote_counter['최민수'] = a, b, c
    # 각 'key'값에 후보이름 할당 후, 위 for문 안에 if, elif를 활용해서 a, b, c값을 'value'값으로 지정
print(vote_counter)     # 'vote_counter'라는 이름의 사전 출력