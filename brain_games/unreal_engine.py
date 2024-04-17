def run_game(game):
    print('Welcome to the Brain Games!')
    user_name = input('May I have your name? ')
    user_name = user_name.capitalize()
    print(f'Hello, {user_name}!')
    print(game.question)
    user_score = 0
    while user_score < 3:
        example, correct_answer = game.question_answer()
        print(example)
        user_answer = input('Your answer: ')
        if str(correct_answer).lower() == user_answer.lower():
            print('Correct!')
            user_score += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'\nLet's try again, {user_name}!")
            break
    if user_score == 3:
        print(f'Congratulations, {user_name}!')
