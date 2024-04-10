def main():
    print('Welcome to the Brain Games!')
    import prompt
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no"')
    i = 0
    while i < 3:
        random_number = randomize()
        even_or_no = even(random_number)
        print(f'Question: {random_number}')
        answer = input('Your answer: ')
        if answer == even_or_no:
            print("Correct!")
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{even_or_no}'.\nLet's try again, {name}!")
            # i = 0
            break
    if i == 3:
        print(f'Congratulations, {name}!')


def randomize():
    from random import randint
    random_number = randint(1, 100)
    return random_number


def even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


if __name__ == '__main__':
    main()
