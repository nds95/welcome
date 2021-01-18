from random import randint

# 랜덤 숫자 뽑기
def generate_number():
    numbers = []
    while len(numbers) < 3:
        i = randint(0, 9)
        if i not in numbers:
            numbers.append(i)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers

# 숫자 받아오기
def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    numbers = []
    while len(numbers) < 3:
        guess = int(input(f"{len(numbers) + 1}번째 숫자를 입력하세요."))
        if guess > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif guess not in numbers:
            numbers.append(guess)
        elif guess in numbers:
            print("중복되는 숫자입니다. 다시 입력하세요.")

    return numbers

# 점수 구하기
def get_score(guesses, solution):

    strike_count = 0
    ball_count = 0

    for i in range(len(guesses)):
        if guesses[i] == solution[i]:
            strike_count += 1
        elif guesses[i] in solution:
            ball_count += 1

    return strike_count, ball_count


# 실행 코드
ANSWER = generate_number()
tries = 0

while tries < 9:
    guess = take_guess()
    s_1, b_1 = get_score(guess, ANSWER)
    if s_1 == 3:
        print(f'축하합니다. {tries}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.')
    else:
        tries += 1
        print(f"S{s_1}, B{b_1}")