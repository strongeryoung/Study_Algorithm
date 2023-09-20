리스트 []

# 지하철 칸별로 10명, 20명, 30명
# subway1= 10
# subway2= 20
# subway3= 30

# subway = [10,20,30]
# print(subway)

# subway = ['박재범','봉준호','BTS']
# print(subway)

# #봉준호씨가 몇 번째 칸에 타고 있는가?
# print(subway.index('봉준호'))

# #조윤주가 다음 정류장에서 다음 칸에 탐
# subway.append('조윤주')
# print(subway)

# # 장원영씨를 박재범 / 봉준호 사이에 태워봄
# subway.insert('장원영',1)
# print(subway)
# subway.insert(1,'장원영')
# print(subway)

# #지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop()) #pop은 어떤 사람을 꺼내는지 확인 가능.
# print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# #같은 이름의 사람이 몇 명 있는지 확인
# subway.append('장원영')
# print(subway)
# print(subway.count('장원영'))

# # 정렬도 가능
# num_list = [5,2,4,3,1]
# num_list.sort() #sort정리 한다
# print(num_list)

# #순서 뒤집기 기능
# num_list.reverse()
# print(num_list)

# # 모두 지우기
# num_list.clear()
# print(num_list)

# #다양한 자료형 함께 사용
# num_list = [5,2,4,3,1]
# mix_list= ['장원영', 20, True]
# #print(mix_list)

# #리스트 확장
# num_list.extend(mix_list)
# print(num_list)

# ##사전
# # cabinet = {3:"봉준호", 100:"박재범"}
# # print(cabinet[3])
# # print(cabinet[100])

# # print(cabinet.get(3)) #이때는 소괄호
# # print(cabinet[5])
# # print(cabinet.get(5,'사용 가능'))
# # print('hi')

# print(3 in cabinet) #True
# print(5 in cabinet) #False

# cabinet = {'A-3':'유재석', 'B-100':'김태호'}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# #새 손님
# print(cabinet)
# cabinet['A-3'] = '김종국'
# cabinet["C-20"]='조세호'
# print(cabinet)

# # 간 손님
# del cabinet['A-3']
# print(cabinet)

# #key 들만 출력
# print(cabinet.keys)

# #value들만 출력
# print(cabinet.values())

# #key, value 쌍으로 출력
# print(cabinet.items())

# #목욕탕 폐점
# cabinet.clear()
# print(cabinet)

# ##튜플
# menu = ('돈까스','치즈 까스')
# print(menu[0])
# print(menu[1])

# #menu.add('생선까스') add라는 것은 존재하지 않는다. 따라서 값을 추가하거나 변경하거나 해야 한다.

# # name = '김종국'
# # age = 20
# # hobby = '코딩'
# # print(name, age, hobby)

# (name, age, hobby) = ('김종국',20,'코딩')
# print(name, age, hobby)

#세트
# 집합 (set)- 중복안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

# java = {'조윤주','강세영','박랑희'}
python = set(['조윤주','악티']) #조윤주는 자바와 파이썬 둘다 가능.

# #교집합 (java와 python을 모두 할 수 있는 개발자)
# print(java&python)
# print(java.intersection(python))

# #합집합 (java도 할 수 있거나 python할 수 있는 개발자)
# print(java|python)
# print(java.union(python)) #순서 보장은 안됨. 그냥 집합에 들어있으면 가능.

# #차집합 (java할 수 있지만 python은 할 줄 모르는 개발자)
# print(java-python)
# print(java.difference(python))

# #python 할 줄 아는 사람이 늘어남
# python.add('김태호')
# print(python)

# #java를 잊었어요
# java.remove("김태호")
# print(java)

# ##자료구조의 변경
# menu = {'커피','우유','주스'}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

# ##퀴즈 4
# # quiz)당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# # 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# # 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# # 추첨 프로그램을 작성하시오.

# # 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# # 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# # 조건3 : random 모듈의 shuffle 과 sample을 활용

# # (출력 예제)
# # -- 당첨자 발표 --
# # 치킨 당첨자 : 1
# # 커피 당첨자 : [2,3,4]
# # -- 축하합니다 --

# # #(활용 예제)
# # from random import *
# # lst = [1,2,3,4,5]
# # # print(1st)
# # # shuffle(1st)
# # # print(1st)
# # print(sample(1st, 1))

# from random import *
# users = range(1, 21) # 1부터 20까지 숫자를 생성
# print(type(users))
# users = list(users)
# print(type(users))

# print(users)
# shuffle(users)
# print(users)

# winners = sample(users, 4) #4명 중에서 1명은 치킨, 3명은 커피

# print("") --당첨자 발표--
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print(" -- 축하합니다 --")

# ##if
# weather = '비'
# # if 조건: 
# #     실행 명령문
# if weather =='비': 
#      print('우산을 챙기세요')

# weather = '미세먼지'
# if weather =='비' or weather == '눈':
#      print('우산을 챙기세요')
# elif weather == '미세먼지':
#      print('마스크를 챙기세요')
# else:
#      print('준비물 필요 없어요')

temp = int(input("기온은 어때요?"))
if 30 <= temp:
     print('너무 더워요. 나가지 마세요')
elif 10 <=temp and temp < 30:
     print('괜찮은 날씨에요')
elif 0 <= temp < 10:
     print('외투를 챙기세요')
else:
     print('너무 추워요. 나가지 마세요')

# print('대기번호 : 1')
# print('대기번호 : 2')
# print('대기번호 : 3')
# print('대기번호 : 4')

#randrange()
for waiting_no in range(1,6):
     print('대기번호 : {0}'.format(waiting_no))

starbucks = ['아이언맨','토르','아이엠 그루트']
for customer in starbucks:
     
