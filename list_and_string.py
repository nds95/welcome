alphabet_list = ['A', 'B', 'C', 'D', 'E']

print(alphabet_list[0])         #A
print(alphabet_list[1])         #B
print(alphabet_list[4])         #E
print(alphabet_list[-1])        #E

alphabet_string = 'ABCDE'

print(alphabet_string[0])       #A
print(alphabet_string[1])       #B
print(alphabet_string[4])       #E
print(alphabet_string[-1])      #E

#string은 list와 비슷함.
#위 처럼 string 형태의 변수에 리스트와 동일한 '[인덱스]'를 사용하여 내용을 갖고오면 list와 동일한 결과값을 가져올 수 있다.

# 하지만 차이점은 list는 인덱스를 수정이 가능하지만, string은 수정이 불가능 하다
#ex)
a = ['a', 'b', 'c']
a[0] = 'f'
print(a)        #['f', 'b', 'c']

a = 'abc'
a[0] = 'f'
print(a)        #TypeError

#string은 수정이 불가능 하지만, string을 합쳐서 새로운 string은 만들 수 있다
#ex)
a = 'abc'
b = 'def'
c = a + b
print(c)            #abcdef