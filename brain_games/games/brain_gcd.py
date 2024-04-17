question = 'Find the greatest common divisor of given numbers.'


def randomize():
    from random import randint
    random_number = randint(1, 100)
    return random_number


def gcd(first_number, second_number):
    gcd = 1
    min_number = min(first_number, second_number)
    for i in range(1, min_number + 1):
        if first_number % i == 0 and second_number % i == 0:
            gcd = i
    return gcd


def question_answer():
    first_number, second_number = randomize(), randomize()
    gcd_number = gcd(first_number, second_number)
    example = f'Question: {first_number} {second_number}'
    correct_answer = gcd_number
    return example, correct_answer
