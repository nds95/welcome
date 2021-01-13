a = 1
b = 1

while b < 10:
    c = a * b
    print(f"{a} * {b} = {c}")
    b += 1
    while b == 10:
        if a < 9:
            b = 1
            a += 1


i = 1

while i <= 9:
    j = 1
    while j <= 9:
        print(f"{i} * {j} = {i*j}")
        j += 1
    i += 1