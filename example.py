# standard library (표준 라이브러리)
import math

print(math.log10(100))

print(math.cos(0))

print(math.pi)

import random

print(random.random())

import os

print(os.getlogin())
print(os.getcwd())

name = input("이름을 입력하세요")  #"이름을 입력하세요"부분은 유저가 입력하기 전에 출력되는 글 / 유저가 입력하기 전까지 코드가 멈춘다.
# input을 이용해서 유저의 입력을 받을 때는 항상 str형태.
# ex)
x = input("숫자를 입력하세요")
print(x + 5)
# 유저입력 = 3
# - 결과 -
#TypeError : can only concatenate str(not "int") to str
# 해결방법
x = int(input("숫자를 입력하세요"))     #input에 int()를 씌워 정수로 형변환
print(x + 5)
