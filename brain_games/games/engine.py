#!/usr/bin/env python3

def welcome():
    print('Welcome to the Brain Games!')


def hello(name, question):
    print(f'Hello, {name.capitalize()}!\n{question}')


def wrong_answer(user_answer, correct_answer, name):
    print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.\nLet's try again, {name.capitalize()}!")


def congrats(count, name):
    if count == 3:
        print(f'Congratulations, {name.capitalize()}!')


def random_operation():
    from random import choice
    seq = (' + ', ' - ', ' * ')
    return (choice(seq))


def random_number():
    from random import randint
    return randint(1, 100)


def question(number_1, number_2, operation=' '):
    print(f'Question: {number_1}{operation}{number_2}')


def answer(operation, number_1, number_2):
    if operation == '+':
        return number_1 + number_2
    elif operation == '-':
        return number_1 - number_2
    elif operation == '*':
        return number_1 * number_2


def gcd(first_number, second_number):
    gcd = 1
    min_number = min(first_number, second_number)
    for i in range(1, min_number):
        if first_number % i == 0 and second_number % i == 0:
            gcd = i
    return gcd


def arithmetic_progression(start, step, quantity):
    list = []
    for i in range(quantity):
        list.append(start)
        start += step
    return list


if __name__ == '__main__':
    main()
