
with open('chicken.txt', 'r') as f:      #open('a', 'b') / a = 파일 이름 / b = 목적(r = read / w = write) / as f 변수로 저장
    for line in f:
        print(line)     #line이라는 변수를 저장 / f변수의 파일을 한줄 씩 가져옴.


# strip = 화이트 스페이스를 없애줌
# 화이트 스페이스 = " ", "\t", "\n"
# 모든 화이트 스페이스를 지우고 싶을 때
# ex)
strip()


# split
# .split("?") = ?를 기준으로 문자열을 리스트로 나눈다.
# split을 이용해서 리스트를 만들면 모두 문자열(str)로 변환된다.
my_string = "1. 2. 3. 4. 5. 6"
print(my_string.split("."))