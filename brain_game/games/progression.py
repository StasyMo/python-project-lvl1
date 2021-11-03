from random import randint


rules = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10
UP_RANGE = 10


def get_question_and_answer():
    common_dif = randint(1, UP_RANGE)
    progression = build_progression(common_dif)
    missed_elem = randint(0, PROGRESSION_LENGTH - 1)
    correct_answer = str(progression[missed_elem])
    question = stringify(progression, missed_elem)
    return question, correct_answer


def build_progression(common_dif: int):
    progression = [randint(0, PROGRESSION_LENGTH)]
    step = 1
    while step < PROGRESSION_LENGTH:
        progression.append(progression[step - 1] + common_dif)
        step += 1
    return progression


def stringify(progression: list, missed_elem: int):
    progression[missed_elem] = '..'
    return " ".join(map(str, progression))
