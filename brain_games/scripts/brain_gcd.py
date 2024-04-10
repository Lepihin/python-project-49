def main():
    from brain_games.games.engine import welcome, hello
    welcome()
    user_name = input('May I have your name? ')
    hello(user_name, 'Find the greatest common divisor of given numbers.')
    from brain_games.games.engine import random_number, question, wrong_answer, congrats, gcd
    user_score = 0
    while user_score < 3:
        first_number = random_number()
        second_number = random_number()
        gcd_number = gcd(first_number, second_number)
        question(first_number, second_number)
        user_answer = input('Your answer: ')
        if user_answer == str(gcd_number):
            print('Correct!')
            user_score += 1
        else:
            wrong_answer(user_answer, gcd_number, user_name)
            break
    congrats(user_score, user_name)


if __name__ == '__main__':
    main()
