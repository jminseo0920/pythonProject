# test
print("hello world")

# 숫자 data type
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

# 문자열 data type
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*3)

#boolean data type 참/거짓
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))

# 애완동물을 소개해 주세요~
animal = "강아지" #고양이
name = "사랑이" #까미
age = 4 #2
hobby = "산책" #헤드번팅
is_adult = age >= 3

print("우리집 "+ animal +" 이름은 "+ name +"예요")
#print(name + "는 " + str(age) + "살이며, "+ hobby + "을 아주 좋아해요")
print(name, "는 ", str(age), "살이며, ", hobby, "을 아주 좋아해요") #띄어쓰기가 무조건 들어감
print(name + " 어른일까요? " + str(is_adult))

#Quiz) 변수를 이용하여 다음 문장을 출력하시오

station = "사당"
# station = "신도림"
# station = "인천공항"
print(station, "행 열차가 들어오고 있습니다.")

#연산자
print(1+1)
print(3-2)
print(5*2)
print(6/3)

print(2++3)
print(5%3)
print(10%3)
print(5//3)
print(10//3)

print(10 > 3)
print(4 >= 7)
print(10 < 3)
print(5 <= 5)

print(3 == 3)
print(4 == 2)
print(3 + 4 == 7)

print(1 != 3)
print(not(1 != 3))

print((3 > 0) and (3 < 5))
print((3 >0) & (3 < 5))

print((3 > 0) or (3 > 5))
print((3 >0) | (3 < 5))

print(5 > 4 > 3)
print(5 > 4 > 7)

#간단한 수식
print(2 + 3 * 4)
print((2 + 3) * 4)
number = 2 + 3 * 4
print(number)
number = number + 2
print(number)
number += 2
print(number)
number *= 2
print(number)
number /= 2
print(number)
number -= 2
print(number)

number *= 2
print(number)
number %= 5
print(number)

print(abs(-5)) # 5
print(pow(4, 2)) # 4^2  = 4*4 = 16
print(max(5, 12)) #12
print(min(5, 12)) #5
print(round(3.14)) # 3
print(round(4.99)) # 5

from math import *
print(floor(4.99)) #내림. 4
print(ceil(3.14)) #올림. 4
print(sqrt(16)) #제곱근. 4

#랜덤함수
from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 미만의 임의의 값 생성

print(int(random() *45) + 1) # 1 ~ 45 미만의 임의의 값 생성 (로또번호)

print(randrange(1, 46)) # 1 ~ 45 미만의 임의의 값 생성 (로또번호)
print(randint(1, 45))

#quiz
#my code
from random import *
print("오프라인 스터디 모임 날짜는 매월 " + str(int(random() * 29) + 4) +"일로 선정되었습니다.")

# for i in range(10):
#     print("오프라인 스터디 모임 날짜는 매월 " + str(int(random() * 25) + 4) + "일로 선정되었습니다.")

from random import *
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) +"일로 선정되었습니다.")

#3/7
sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

#슬라이싱
jumin = "990120-1234567"

print("성별 : " +jumin[7])
print(" 연 : " +jumin[0:2]) #:~부터 직전까지
print("월 : " +jumin[2:4])
print("일 : " +jumin[4:6])

print("생년월일 : " + jumin[:6]) #처음부터 6직전까지
print("뒤 7자리 : " + jumin[7:14]) # = [7:]
print("뒤 7자리 (뒤에서부터) : " + jumin[-7:]) #맨 뒤에서 7번째부터 끝까지

#문자열 처리함수
python = "Python is Amazing"
print(python.lower()) #소문자 변환
print(python.upper()) #대문자 변환
print(python[0].isupper()) #[]가 대문자인지 T/F
print(len(python)) #글자수
print(python.replace("Python", "Java")) #문자열 변화

index = python.index("n")
print(index)
index = python.index("n", index + 1) #찾은 위치에서 1번째 뒤부터 찾기
print(index)

print(python.find("Java")) #없으면 -1
print(python.index("Java")) #없으면 오류 다음 코드 진행 불가
print("hi")

print(python.count("n")) #n이 변수에서 몇번나오는지

#문자열 포멧
print("a" + "b")
print("a" , "b")

#방법 1
print("나는 %d살입니다." % 20) #d숫자
print("나는 %s을 좋아해요." % "파이썬") #s 문자열
print("Apple 은 %c로 시작해요. " % "A") #c 문자
#%s
print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

#방법 2
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))

#방법3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age = 20))

#방법4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

#탈출문자
