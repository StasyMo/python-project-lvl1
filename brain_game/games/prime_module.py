from random import randint
from brain_game.games.engine_of_game import comparing_answers
from brain_game.games.correct_answers import prime_correct_answer


def prime_game(user_name, count_answers, ANSWERS_TO_WIN):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while count_answers < ANSWERS_TO_WIN:
        UP_RANGE = 1000
        question_number = randint(1, UP_RANGE)
        print('Question: {}'.format(question_number), '\nYour answer: ', end='')
        user_answer = input()
        correct_answer = prime_correct_answer(question_number)
        count_answers = comparing_answers(correct_answer, user_answer,
                                          count_answers, ANSWERS_TO_WIN,
                                          user_name)
        count_answers += 1
    return count_answers
