# 화씨를 섭씨로 바꿔주는 함수
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

temperature_list = [40, 15, 32, 64. -4, 11]
print("화씨 온도 리스트: " + str(temperature_list)) # 화씨 온도 출력

i = 0

while i < len(temperature_list): #i가 temperature_list 범위보다 작을 때까지 반복
    temperature_list[i] = round(fahrenheit_to_celsius(temperature_list[i]), 1) #리스트에 함수를 넣고 파라미터에 'i'를 넣어 각 인덱스 요소가 계산되게 설정
    i += 1 #인덱스 요소를 순서대로 계산하기 위한 코드

print("섭씨 온도 리스트: " + str(temperature_list)) # 섭씨 온도 출력