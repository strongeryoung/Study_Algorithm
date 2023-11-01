# Study : final project_hangman


import random

def choose_word():
    word_list = ["python", "study", "akti", "minseok", "seyoung", "love", "sejong", "yoonju", "ranghee", "gunwoo", "hungry", "christmas"]
    return random.choice(word_list)

def display_word(word, guessed_letters):   # 현재까지 맞춘 글자와 아직 맞추지 못한 글자를 표시하고, 남은 횟수를 표시하는 함수 
    display = ""           # 부분적으로 맞춘 글자를 저장
    for letter in word:    # word 에 있는 각 글자를 반복해서 확인, word 는 맞춰야하는 단어(정답)를 나타냄
        if letter in guessed_letters:   # letter 가 맞춘 글자목록에 포함되어 있는지 확인, 포함되어 있다면 - 이미 맞춘 글자이므로 display 에 추가
            display += letter
        else:              # 그렇지 않으면 display에 언더스코어 추가          
            display += "_"
    return display

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 10  # 틀린 시도 횟수

    print("행맨게임을 시작합니다 ~~~")
    
    while True:
        if attempts <= 0:
            print("횟수를 초과하였습니다! 정답은", word_to_guess)
            break

        print("\nWord:", display_word(word_to_guess, guessed_letters), ", 글자 수 : ", len(word_to_guess))   #현재까지 맞춘 글자와 단어의 길이를 출력하여 플레이어에게 현재 게임 상태를 보여줌
        print("남은 횟수:", attempts)

        guess = input("한 글자씩 맞혀주세요! : ").lower()  #플레이어에게 한 글자를 입력하도록 요청하고, 사용자 입력을 소문자로 변환한 후 guess 변수에 저장

        if len(guess) != 1 or not guess.isalpha(): #사용자 입력이 한 글자가 아니거나 알파벳 문자가 아닌 경우, 오류 메시지를 출력하고 continue를 사용하여 현재 반복을 종료하고 다음 반복을 시작
            print("한 글자씩 입력해주세요.")
            continue

        if guess in guessed_letters:   #만약 guess가 이미 추측한 글자 목록인 guessed_letters에 포함되어 있다면, "I am 했던 글자예요." 메시지를 출력하고 continue를 사용하여 현재 반복을 종료하고 다음 반복을 시작
            print("I am 했던 글자예요.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:  # 플레이어가 이미 추측한 글자 목록인 guessed_letters에 포함되어 있다면, "I am 했던 글자예요." 메시지를 출력하고 continue를 사용하여 현재 반복을 종료하고 다음 반복을 시작
            print("WOW ~ 있는 글자입니다")
            if set(word_to_guess) == set(guessed_letters):
                print("Congratulations! 정답입니다 ~~~", word_to_guess)
                break
            
        if len(word_to_guess) == len(guessed_letters):     #: 플레이어가 모든 글자를 맞추었는지 확인하는 조건. set(word_to_guess)는 정답 단어에 있는 모든 글자를 집합으로 나타내고, set(guessed_letters)는 플레이어가 추측한 글자를 집합으로 나타냅니다. 만약 두 집합이 같다면, 모든 글자를 맞추었다는 뜻이므로 "Congratulations! 정답입니다 ~~~" 메시지를 출력하고 게임을 종료
            if set(word_to_guess) == set(guessed_letters):
                print("정 ! 답 ! 입니다 ~~~ 혹시 당신은 천재?", word_to_guess)    # 중간에 정답을 쓸 수 있는 기회...를 주고 싶었음... 시간 관계 상 실행되지 않는 걸로.....
                break

        else:
            print("때애애애애애애애애앵~~~~~~~~!")
            attempts -= 1


if __name__ == "__main__":
    hangman()  #
