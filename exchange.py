def krw_to_usd(krw):    # 원화를 달러
    # 로 변환하는 함수
    return krw / 1000

def usd_to_jpy(usd):    # 달러를 엔화로 변환하는 함수
    return usd * 125


prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]   # 원화에 대한 금액 리스트
print("한국 화폐: " + str(prices)) # 가격에 대한 원화로 된 리스트(string 형변환)

i = 0   # 카운트를 하기위한 함수 정의

while i < len(prices):          # 'prices'리스트 범위에 도달할 때 까지 반복
    prices[i] = krw_to_usd(prices[i])       # 리스트 인덱스에 원화를 달러로 변환한 값으로 치환
    i += 1
print("미국 화폐: " + str(prices))

i = 0

while i < len(prices):
    prices[i] = usd_to_jpy(prices[i])
    i += 1

print("일본 화폐: " + str(prices))