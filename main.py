count = 1
a = 0
b = 1
print(1)

while count < 50:
    b = a + b
    a = b - a
    print(b)
    count += 1