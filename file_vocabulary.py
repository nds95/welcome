# 단어장 프로그램 만들기
exit_word = "q"         #exit_word에 원하는 종료단어를 입력
while True:             #무한반복
    eng_word = input("영어 단어를 입력하세요:")           #유저가 입력한 값을 'eng_word' 변수에 입력
    with open("vocabulary.txt", "a") as W:          #vocabulary파일을 append 전용으로 불러오고 W라고 지정
        if eng_word != exit_word:                   #eng_word가 exit_word와 일치하지 않을 때 실행
            W.write(f"{eng_word}: ")                #eng_word를 W변수 파일에 입력
            kor_word = input("한국어 뜻을 입력하세요:")   #다음 차례인 한국어 입력으로 넘어감
            if kor_word != exit_word:               #kor_word가 exit_word와 일치하지 않을 때 실행
                W.write(f"{kor_word}\n")            #kor_word를 W변수에 입력 후 줄을 바꾼다.
            else:
                break
        else:
            break                                   #if문이 실행되지 않을 때 프로그럼을 종료한다.