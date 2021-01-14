#for문을 이용하여 list 요소들의 순서 뒤집기
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

for i in range(len(numbers)):
    a = -1
    numbers.insert(i, numbers[a])
    del numbers[a]
    a -= 1

print(numbers)