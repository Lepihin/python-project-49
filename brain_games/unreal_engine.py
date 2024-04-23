def run_game(game):
    print('Welcome to the Brain Games!')
    user_name = input('May I have your name? ')
    user_name = user_name.capitalize()
    print(f'Hello, {user_name}!')
    print(game.question)
    USER_SCORE = 3
    for i in range(USER_SCORE):
        example, correct_answer = game.question_answer()
        print(example)
        user_answer = input('Your answer: ')
        if str(correct_answer).lower() == user_answer.lower():
            print('Correct!')
        else:
            return print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'\nLet's try again, {user_name}!")
    print(f'Congratulations, {user_name}!')
