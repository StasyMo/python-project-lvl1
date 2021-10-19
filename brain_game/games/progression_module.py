from random import randint
from brain_game.games.engine_of_game import comparing_answers
from brain_game.games.correct_answers import progression_correct_answer


def progression_game(user_name, count_answers, ANSWERS_TO_WIN):
    PROGRESSION_LENGTH = 10
    UP_RANGE = 10
    print('What number is missing in the progression?')
    while count_answers < ANSWERS_TO_WIN:
        progression = [0] * PROGRESSION_LENGTH
        progression[0] = randint(0, UP_RANGE)
        progression_step = randint(1, UP_RANGE)
        missed_elem = randint(0, UP_RANGE - 1)
        i = 1
        print('Question: ', end='')
        correct_answer = progression_correct_answer(progression,
                                                    progression_step,
                                                    missed_elem, i,
                                                    PROGRESSION_LENGTH)
        print('Your answer: ', end='')
        user_answer = input()
        try:
            user_answer = int(user_answer)
        except ValueError:
            return print("The answer might be a number, but '{0}' "
                         "is not a number ;(. \n Let's try again, "
                         "{1}!".format(user_answer, user_name))
        count_answers = comparing_answers(correct_answer, user_answer,
                                          count_answers,
                                          ANSWERS_TO_WIN, user_name)
        count_answers += 1
    return count_answers
