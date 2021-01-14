# range를 활용한 리스트 인덱스 및 요소 출력하기

numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]          # numbers 리스트 정의

for i in range(len(numbers)):           # range 범위에 'len(numbers)'라고 지정하여 리스트 범위가 변동되도 그대로 가져와 실행할 수 있도록 설정
    print(i, numbers[i])            #print(인덱스, 요소)