# 자리수 합 리턴
def sum_digit(num):     # 'sum_digit'라는 함수를 만듦 / num이라는 이름으로 파라미터를 가지고 온다.
    total = 0           # 각 자리수 합을 갖고와 저장하는 변수
    a = str(num)        # 정수의 숫자를 각 자리수 별로 나누기 위해 str으로 class 정의
    for i in a:         # i 변수가 a의 인덱스 수 까지 실행
        total += int(i) # total에 a 각 자리수의 숫자(i자리에 있는 값을 정수로 전환)를 계속 더함
    return total        # total값을 num에 리턴

a = 0
b = 0
while a < 1000:         # a가 1000보다 작을 동안 실행
    a += 1              # while문이 실행 될 때 마다 a에 1씩 더함
    b += sum_digit(a)   # b에 sum_digit(a) 결과값을 계속 더함

print(b)