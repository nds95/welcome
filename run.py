# area 모듈 갖고오기
import area

print(area.square(3))

# area모듈 안에 함수 갖고오기
from area import square

#area모듈 이름 바꾸기
import area as ar

#area모듈 안에 있는 함수 이름 바꾸기
from area import square as sq

#area 안에 있는 정의된 이름들 불러오기
print(dir(area))

#현재 파일안에 있는 정의된 이름들 불러오기
#print(dir)

#name space = 파일에서 정의된 모든 이름
#dir함수는 ()안에 있는 정의된 모든 이름들을 리턴해주는 함수

