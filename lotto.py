from random import randint

# 랜덤 수 n개 만큼 구하기
def generate_number(n):
    lottey = []
    while len(lottey) < n:
        random_numbers = randint(1, 45)
        if random_numbers not in lottey:
            lottey.append(random_numbers)

    return lottey

# 당첨 번호 구하기
def draw_winning_numbers():
    winning_numbers = []
    while len(winning_numbers) < 7:
        random_numbers = randint(1, 45)
        if random_numbers not in winning_numbers and len(winning_numbers) <= 6:
            winning_numbers.append(random_numbers)
            if len(winning_numbers) == 6:
                winning_numbers.sort()
        elif random_numbers not in winning_numbers and len(winning_numbers) == 7:
            winning_numbers.append(random_numbers)

    return winning_numbers

print(draw_winning_numbers())
