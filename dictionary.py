# 사진(dictionary)
# key-value pair (키와 값이 쌍을 이룬다)

my_dictionary = {
    5: 25,          # 5 : key / 25 : value(값)
    2: 4,
    3: 9
}

print(my_dictionary[3])         # key 3의 값인 9가 출력 된다.

# dict에 키 추가하기
my_dictionary[9] = 81           #대괄호 안에 키를 입력 후 지정연산자 '='을 사용, 오른쪽에 값을 입력

# '사전'에는 리스트와는 다르게 키(인덱스) 값이 정수형이 아니여도 된다.
#ex)
my_family = {
    '엄마': '김김김',
    '아빠': '이이이',
    '나': '이루루'
}
print(my_family)        #{'엄마': '김김김', '아빠': '이이이', '나': '이루루'}

# 사전에 '값' 불러오기
print(my_family.values())

# 사전에 '값' 찾아내기
print('김김김' in my_family.values())      #True / False
print(my_family[key])