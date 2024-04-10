from brain_games.games.engine import random_operation, random_number
from brain_games.games.engine import question, answer


def main():
    user_score = 0
    print('Welcome to the Brain Games!')
    user_name = input('May I have your name? ')
    user_name = user_name.capitalize()
    print(f'Hello, {user_name}!\nWhat is the result of the expression?')
    while user_score < 3:
        number_1, number_2 = random_number(), random_number()
        operation = random_operation()
        question(number_1, number_2, operation)
        ai_answer = answer(operation, number_1, number_2)
        user_answer = input('Your answer: ')
        if str(ai_answer) == user_answer:
            print('Correct!')
            user_score += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{ai_answer}'\nLet's try again, {user_name}!")
            break
        if user_score == 3:
            print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
