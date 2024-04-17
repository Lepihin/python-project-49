question = 'What is the result of the expression?'


def random_number():
    from random import randint
    return randint(1, 100)


def random_operation():
    from random import choice
    seq = (' + ', ' - ', ' * ')
    return (choice(seq))


def calc(operation, number_1, number_2):
    if operation == ' + ':
        return number_1 + number_2
    elif operation == ' - ':
        return number_1 - number_2
    elif operation == ' * ':
        return number_1 * number_2


def question_answer():
    number_1, number_2 = random_number(), random_number()
    operation = random_operation()
    example = f'Question: {number_1}{operation}{number_2}'
    correct_answer = calc(operation, number_1, number_2)
    return example, correct_answer
