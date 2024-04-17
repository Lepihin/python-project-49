question = 'Answer "yes" if the number is even, otherwise answer "no".'


def randomize():
    from random import randint
    random_number = randint(1, 100)
    return random_number


def even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def question_answer():
    random_number = randomize()
    even_or_no = even(random_number)
    example = f'Question: {random_number}'
    correct_answer = even_or_no
    return example, correct_answer
