from brain_games.games.engine import welcome, hello, random_number
from brain_games.games.engine import is_prime, wrong_answer, congrats


def main():
    welcome()
    user_name = input('May I have your name? ')
    hello(user_name, 'Answer "yes" if given number is prime.\
 Otherwise answer "no".')
    user_score = 0
    while user_score < 3:
        random = random_number()
        print(f'Question: {random}')
        user_answer = input('Your answer: ')
        correct_answer = is_prime(random)
        if user_answer.upper() == correct_answer.upper():
            print('Correct!')
            user_score += 1
        else:
            wrong_answer(user_answer, correct_answer, user_name)
            break
    congrats(user_score, user_name)


if __name__ == '__main__':
    main()
