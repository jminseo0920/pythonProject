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
print("백문이 불여일견 \n백견이 불여일타")

#\"\'
#저는 "정민서" 입니다.
print("저는 \"정민서\" 입니다.")

#\\ : 문장 내에서 \
print("C:\\Users\\t\Documents\\Git\\pythonProject")

#\r : 커서를 맨 앞으로 이동
print("Red Apple\rpine")

# \b : 백스페이스 (한글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")

#quiz 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

#예) http://naver.com
#규칙1 : http:// 부분은 제외
#규칙2 : 처음 만나는 점(.) 이후 부분은 제외
#규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
#예) 생성한 비밀번호 : nav51!

#my code
site = "http://naver.com"
rule1 = site[7:]
print(rule1)
rule2 = rule1[:-4]
print(rule2)
rule3 = rule2[:3] + str(len(rule2)) + str(rule2.count("e")) +"!"
print(rule3)

url = "http://naver.com"
my_str = url.replace("http://","") #규칙1
#print(my_str)
my_str = my_str[:my_str.index(".")] #규칙2
#print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1}입니다.".format(url, password))

# 3/12
#리스트 []

#지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

#조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

#하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈")

#지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway) #하하

print(subway.pop())
print(subway) #박명수

print(subway.pop())
print(subway) #조세호

#같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
num_list = [5,2,4,3,1]
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)

# 사전
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet[5]) #오류 및 프로그램 종료

print(cabinet.get(5)) #None 출력 후 계속 실행
print(cabinet.get(5, "사용 가능"))

print(3 in cabinet) #X in 변수  True
print(5 in cabinet) #X in 변수  False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 페점
cabinet.clear()

# 튜플 -> 내용 변경 및 삭제가 안됨 근데 리스트보다 속도가 빠름
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

menu.add("생선까스") #오류

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

name, age, hobby = ("김종국", 20, "코딩")
print(name, age, hobby)

# 3/14
# 집합
# 중복 안됨, 순서 없음
my_set  = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석","박명수"])

# 교집합 (java 와 python 을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java 할 수 있거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java 할 수 있지만 python 할 수 없음)
print(java - python)
print(java.difference(python))

# python을 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java 를 까먹음
java.remove("김태호")
print(java)

#3/18
# 자료구조의 변경
# 커피숍
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

# quiz
# 당신의 학교에서는 파이썬 코딩 대화를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다. 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오

#ex
# from random import *
# 1st = [1,2,3,4,5]
# print(1st)
# shuffle(1st)
# print(1st)
# print(sample(1st,1))

# my answer code
# from random import *
# event = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# shuffle(event)
# event1 = sample(event,1)
#
# event = event.difference(event1)
# shuffle(event)
# event2 = sample(event,3)
#
# print("--당첨자 발표--" \n )
# print(event2)

# answer code
from random import *
users = range(1,21)
# print(type(users))
users = list(users)
# print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users, 4)

print(" --당첨자 발표-- ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print(" -- 축하합니다 -- ")

# 3/19
# if
weather = input("오늘 날씨는 어때요? ")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물이 필요 없어요")

temp = int(input("기온은 어때요? ")) # 기온의 특징상 int를 붙임
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp and temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요 나가지 마세요")

# # for
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# for waiting_no in [0, 1, 2, 3, 4]:
#     print("대기번호 : {0}".format(waiting_no))
for waiting_no in range(1, 6):
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))

# while
customer = "토르"
index = 5
while index >= 1:
    print("{0},손님 커피가 준비되었습니다. {1} 번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

customer = "아이언맨"
while True:
    print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer, index))
    index += 1

customer = "토르"
person = "Unknown"

while person != customer:
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")

# 3/20
# continue and break
absent = [2, 5] # 결석
no_book = [7] # 책을 깜박함
for student in range(1, 10):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print(" {0}, 책을 읽어봐".format(student))

# 한줄 for
# 출석번호 1, 2, 3, 4 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생들 이름을 길이로 변환
students = ["Iron man", "Thor", "Groot"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "Groot"]
students = [i.upper() for i in students]
print(students)

# Quiz
# 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# my answer code
for customers in range(1, 51):
    time = randrange(5, 50)
    if time <= 15:
        check = "O"
    else:
        check = ""
        print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(check, customers, time))
        continue
    print("총 탑승 승객 : {0} 분".format(check.count("O")))

# answer code
from random import *
cnt = 0
for i in range(1,51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0} 분".format(cnt))

# 내 코드는 time도 잘못 설정, randrange도 잘못설정, 총 탑승 승객 수 파악 구현 실패

# 함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")
# 이 상태에선 실행해도 아무런 변화가 없음
open_account()
# 함수 호출을 해줘야 실행됨

# 전달값과 반환값
def deposit(balance, money): #입금
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money
def withdraw(balance, money): #출금
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100
    return commission ,balance - money - commission

balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))

# 기본값
# def profile(name, age, main_lang):
#     print(f"이름 : {name}\t나이 : {age}\t주 사용 언어: {main_lang}")

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업.
def profile(name, age=17, main_lang="파이썬"):
    print(f"이름 : {name}\t나이 : {age}\t주 사용 언어: {main_lang}")

profile("유재석")
profile("김태호")

# 3/25
# 키워드값
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name = "유재석", main_lang = "파이썬", age = 20)
profile(main_lang = "자바""김태호", age = 25, name = "김태호")

# 가변인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print(f"이름 : {0}\t나이 : {1}\t".format(name, age), end = "")
#     print(lang1, lang2, lang3, lang4, lang5)
#
def profile(name, age, *language):
    print(f"이름 : {0}\t나이 : {1}\t".format(name, age), end="")
    for lang in language:
        print(lang, end="")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotiln", "Swift")









