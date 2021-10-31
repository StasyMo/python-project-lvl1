from random import randint


rules = 'What number is missing in the progression?'


def get_question_and_answer():
    progression_length = 10
    up_range = 10
    progression = build_progression(progression_length, up_range)
    missed_elem = randint(0, progression_length - 1)
    correct_answer = str(progression[missed_elem])
    question = stringify(progression, missed_elem)
    return question, correct_answer


def build_progression(progression_length: int, up_range: int):
    progression = [randint(0, up_range)]
    common_dif = randint(1, up_range)
    step = 1
    while step < progression_length:
        progression.append(progression[step - 1] + common_dif)
        step += 1
    return progression


def stringify(progression: list, missed_elem: int):
    progression[missed_elem] = '..'
    return " ".join(map(str, progression))
