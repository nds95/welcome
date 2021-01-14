numbers = []
print(numbers)

numbers.append(1)
numbers.append(7)
numbers.append(3)
numbers.append(6)
numbers.append(5)
numbers.append(2)
numbers.append(13)
numbers.append(14)
print(numbers)

i = len(numbers) - 1
while i >= 0:
    if numbers[i] % 2 != 0:         # i순서의 인덱스 요소의 숫자가 2로 나눠서 0이 아닐 때
        del numbers[i]              # 해당 인덱스를 지운다.
    i -= 1
print(numbers)

numbers.insert(0, 20)           #(a, b) a는 인덱스 순서 / b는 insert할
print(numbers)

print(sorted(numbers))

print("Hello")