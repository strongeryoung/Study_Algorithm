
# 190 / 알고리즘 1. 냅다 프린트 노가다
apart = [[101, 102], [201, 202], [301, 302]]

print(apart[0][0],"호")
print(apart[0][1],"호")
print(apart[1][0],"호")
print(apart[1][1],"호")
print(apart[2][0],"호")
print(apart[2][1],"호")

# 190 / 알고리즘 2. 함수로 정의하기

apart = [[101, 102], [201, 202], [301, 302]]

def solution(apart):
    answer = print([],"호")
    for i in apart:
        answer += i[0]
    return answer


# 210 / 실행결과 예측하기

def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()


# 3문제 (클래스)
# 1. 본인의 관심 분야의 클래스를 정의해보기 - 생성자 및 다양한 메서드 추가
# 2. 여러 객체를 생성하기
# 3. 1번에서 정의한 클래스를 상속받는 새로운 클래스를 정의해보기

# 1. IVE 클래스 정의
class IVE:
    def __init__(self, name, position, age):
        self.name = name
        self.position = position
        self.age = age
        self.is_active = True  # 멤버가 활동 중인지 여부를 나타내는 기본값 설정

    def introduce(self):
        return f"안녕하세요, 저는 IVE의 {self.position} {self.name}입니다."

    def get_age(self):
        return f"{self.name}의 나이는 {self.age}세 입니다."

    def set_activity_status(self, status):
        self.is_active = status

# 2. 여러 객체 생성하기 (IVE 멤버)
yujin = IVE("안유진", "리더", 24)
liz = IVE("리즈", "메인 보컬", 22)
wonyoung = IVE("장원영", "서브 보컬", 21)

print(yujin.introduce())
print(liz.get_age())
print(wonyoung.introduce())

# 3. IVE 클래스를 상속받는 새로운 클래스 정의
class TraineeIVE(IVE):
    def __init__(self, name, age, training_period):
        super().__init__(name, "연습생", age)
        self.training_period = training_period

    def introduce(self):
        return f"안녕하세요, 저는 IVE의 연습생 {self.name}입니다. 연습 기간은 {self.training_period} 개월입니다."

# 새로운 클래스 객체 생성
trainee_jane = TraineeIVE("제인", 20, 12)

print(trainee_jane.introduce())
