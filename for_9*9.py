# for문을 이용한 구구단 만들기


for i in range(1, 10):          #'단'단위에 해당되는 for문
    for j in range(1, 10):          # *뒤에 들어갈 수의 for문
        print(f"{i} * {j} = {i*j}")     # format기능을 활용한 print 구현