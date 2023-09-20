# 함수

def open_account():
    print("새로운 계좌가 생성되었습니다.")

# open_account()

def deposit(balance, money): # 입금
    print("입금이 완료되었습니다. 잔액은 {0} 원 입니다.". format(balance + money))
    return balance + money 

def withdraw(balance, money): # 출금
    if balance >= money: # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance

def withdraw_night(balance, money): # 저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance - money - commission 

balance = 0 # 잔액
balance = deposit(balance, 1000)
# print(balance)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))


# 함수 기본값 설정

def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용언어: {2}" \
          .format(name, age, main_lang))   # 역슬러시로 줄바꿈 - 두 줄이 한줄임
    
profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")


# 같은 학교 같은 학년 같은 반 같은 수업. - 이름만 다르고 나이, 수업 같음

def profile(name, age = 17, main_lang = "파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용언어: {2}" \
          .format(name, age, main_lang))
    
profile("유재석")
profile("김태호")


# 키워드 값을 이용한 함수 호출

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name = "유재석", main_lang = "파이썬", age = 20)
profile(main_lang = "자바", age = 25, name = "김태호")


# 가변인자를 활용한 함수 호출  

def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이: {1}\t".format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)


# 가변인자 *로 시작되는 매개변수를 활용하여 6개의 언어를 입력하면 6개의 언어가, 2개의 언어를 입력하면 2개의 언어가 출력됨
# 서로 다른 갯수의 값을 넣어줄때는 가변인자 *을 사용할 수 있음

def profile(name, age, *language):
    print("이름 : {0}\t나이: {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")


# 지역변수와 전역변수

# 지역변수 : 함수 내에서만 쓸 수 있는 것, 함수가 호출됐을 때 만들어졌다가 함수 호출이 끝나면 사라지는 것
# 전역변수 : 모든 공간에서 부를 수 있는 변수

# gun = 10

# def checkpoint(soldiers): # 경계근무
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계 근무 나감
# print("남은 총 : {0}".format(gun))

#  ㄴ 오류 : gun이라는 함수가 할당도 안됐는데, 값이 설정도 안되었는데 사용되어서 오류가 남.
#  ㄴ gun = 10 이 함수 밖에서 초기화 됨. 따라서, 함수 내에서 gun = 10 이라고 초기화를 해야 함.
#  ㄴ 이게 바로 "지역변수" ! 

# 수정한 올바른 코드
gun = 10

def checkpoint(soldiers): # 경계근무
    gun = 20
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명이 경계 근무 나감
print("남은 총 : {0}".format(gun))


# 전역변수 사용 예

gun = 10

def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun # 외부에서 건이라는 함수를 정의 쳌포인트렛 함수 호출

print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계 근무 나감
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))

# Quiz) 표준 체중을 구하는 프로그램을 작성하시오.

# 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#         * 함수명 : std_weight
#         * 전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender): # 키는 m단위 (실수), 성별 "남자"/ "여자"
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21
    
height = 175 # cm단위
gender = "남자"
weight = round(std_weight(height / 100, gender), 2) # round함수를 통해 소수점 둘째자리까지 표시
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))


# 표준 입출력

print("Python", "Java", sep=" vs ") # sep= "" 파이썬과 자바 사이에 들어갈 것을 정함
print("Python", "Java", sep=",", end="?") # 문장의 끝부분을 물음표로 바꿔주고, 다음 코드를 이어서 출력함. (줄 바꾸지않고)
print("무엇이 더 재밌을까요?")

import sys
print("Python", "Java", file=sys.stdout) # 표준 출력으로 출력
print("Python", "Java", file=sys.stderr) # 표준 에러로 출력


# 시험 성적

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
