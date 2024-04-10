from random import randint
from brain_games.games.engine import welcome, hello, wrong_answer, congrats, arithmetic_progression

def main():
    welcome()
    user_name = input('May I have your name? ')
    hello(user_name, 'What number is missing in the progression?')
    user_score = 0
    while user_score < 3:
        list = arithmetic_progression(randint(1,10),randint(1,5), randint(5,10))
        random_number = randint(0, len(list)-1)
        hidden = list[random_number]
        list[random_number] = '..'
        progression = ''
        for i in range(0, len(list)):
            progression += str(list[i])+' '
        print(f'Question: {progression}')
        user_answer = input('Your answer: ')
        if user_answer == str(hidden):
            print('Correct!')
            user_score += 1
        else:
            wrong_answer(user_answer, hidden, user_name)
            break
    congrats(user_score, user_name)



if __name__ == '__main__':
    main()
