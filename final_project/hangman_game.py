# Study : final project_hangman


import random

def choose_word():
    word_list = ["python", "study", "akti", "minseok", "seyoung", "love", "sejong", "yoonju", "ranghee", "gunwoo", "hungry", "christmas"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
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

        print("\nWord:", display_word(word_to_guess, guessed_letters), ", 글자 수 : ", len(word_to_guess))
        print("남은 횟수:", attempts)

        guess = input("한 글자씩 맞혀주세요! : ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("한 글자씩 입력해주세요.")
            continue

        if guess in guessed_letters:
            print("I am 했던 글자예요.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("WOW ~ 있는 글자입니다")
            if set(word_to_guess) == set(guessed_letters):
                print("Congratulations! 정답입니다 ~~~", word_to_guess)
                break
            
        if len(word_to_guess) == len(guessed_letters):
            if set(word_to_guess) == set(guessed_letters):
                print("정 ! 답 ! 입니다 ~~~ 혹시 당신은 천재?", word_to_guess)    # 중간에 정답을 쓸 수 있는 기회...를 주고 싶었음... 시간 관계 상 실행되지 않는 걸로.....
                break

        else:
            print("때애애애애애애애애앵~~~~~~~~!")
            attempts -= 1


if __name__ == "__main__":
    hangman()
