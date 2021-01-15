import random       #random 모듈 import

random_result = random.randint(1, 20)       #random_result에 랜덤값 정
chance = 4                                  #기회는 4번
while chance >= 1:                          #chance가 1이상일 때 반복
    in_put = int(input(f"기회가 {chance}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: "))  #in_put변수에 유저입력값을 정수로 받음
    if in_put == random_result:
        print(f"축하합니다. {chance}번 만에 숫자를 맞히셨습니다.")       #만약 정답일 시, 현재 남은 chance를 알려주며 끝낸다.
        break
    elif chance == 1:                                         #chance가 최종 1이 됐을 때는 실행 되므로, 끝나는 조건을 1로 한다.
        print(f"아쉽습니다. 정답은 {random_result}입니다.")
        break
    elif in_put > random_result:
        chance -= 1                                           #입력이 random_result보다 클 때 'Down'을 알려주고 chance를 1 깎는다.
        print("Down")
    elif in_put < random_result:
        chance -= 1
        print("Up")