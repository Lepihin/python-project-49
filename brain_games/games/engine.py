#!/usr/bin/env python3


def random_operation():
    from random import choice
    seq = ('+', '-', '*')
    return (choice(seq))


def random_number():
    from random import randint
    return randint(1, 100)


def question(number_1, operation, number_2):
    print(f'Question: {number_1} {operation} {number_2}')


def answer(operation, number_1, number_2):
    if operation == '+':
        return number_1 + number_2
    elif operation == '-':
        return number_1 - number_2
    elif operation == '*':
        return number_1 * number_2


if __name__ == '__main__':
    random_operation()
