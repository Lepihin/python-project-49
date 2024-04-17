from random import randint

question = 'Answer "yes" if given number is prime.\
 Otherwise answer "no".'


def randomize():
    random_number = randint(1, 100)
    return random_number


def is_prime(n):
    if n <= 1:
        return 'No'
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 'No'
    return 'Yes'


def question_answer():
    first_number = randomize()
    correct_answer = is_prime(first_number)
    example = f'Question: {first_number}'
    return example, correct_answer
