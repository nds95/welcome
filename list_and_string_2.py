# 주민등록번호 뒤 4자리 가리기

def mask_security_number(security_number):
    a = security_number[:-4]            # a변수에 security_number로 가져온 문자열을 인덱스 -4까지 슬라이스한 결과를 정의
    b = a + '****'                      # b변수에 a값 + 문자열 '****'을 합친다.
    return b                            # b값을 security_number에 return한다.


print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))