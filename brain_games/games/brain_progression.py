from random import randint


question = 'What number is missing in the progression?'


def question_answer():
    start = randint(1, 10)
    step = randint(1, 5)
    quantity = randint(5, 10)
    list = arithmetic_progression(start, step, quantity)
    random_number = randint(0, len(list) - 1)
    hidden = list[random_number]
    list[random_number] = '..'
    progression = ' '.join(map(str, list))
    example = f'Question: {progression}'
    correct_answer = hidden
    return example, correct_answer


def arithmetic_progression(start, step, quantity):
    list = []
    for i in range(quantity):
        list.append(start)
        start += step
    return list
