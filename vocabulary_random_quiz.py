import random as rd

questions = []
with open("vocabulary.txt", "r") as f:
    for line in f:
        list = line.strip().split(": ")     #list변수에 f파일에 있는 모든 내용을 빈 공간없이 리스트화
        questions += list
    while True:
        random_result = rd.randrange(0, len(questions), 2)          #랜덤수를 질문에 맞게 0부터 짝수만 나오게 함
        answer = input(f"{questions[random_result]}:")              #리스트의 짝수 인덱스를 문제로 출력
        if answer == questions[random_result+1]:
            print("맞았습니다!")
        elif answer == "q": 
            break
        else:
            print(f"틀렸습니다. 정답은 {questions[random_result+1]}입니다.")