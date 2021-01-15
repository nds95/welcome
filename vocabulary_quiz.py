# 단어장 퀴즈 프로그램

with open("vocabulary.txt", "r") as f:          #vocabulary.txt파일을 읽기전용으로 갖고와 f변수에 정의
    for line in f:                              #for문으로 한줄 씩 불러냄
        quiz = line.strip().split(": ")[0]      #quiz변수에 각 줄을 split으로 리스트화 시켜 0번 인덱스에 있는 값을 저장
        answer = input(f"{quiz}:")              #answer에 유저가 기입한 값을 저장하고, quiz변수를 문제로 냄
        if answer == line.strip().split()[1]:   #문제와 답이 같을 때 실행
            print("맞았습니다!")
        else:                                   #문제와 답이 다를 때 실행
            print(f"아쉽습니다. 정답은 {quiz}입니다.")
