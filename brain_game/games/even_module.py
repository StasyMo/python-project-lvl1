from random import randint
from brain_game.games.engine_of_game import comparing_answers
from brain_game.games.correct_answers import even_correct_answer


def even_game(user_name, count_answers, ANSWERS_TO_WIN):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while count_answers < ANSWERS_TO_WIN:
        number_up_range = 1000000
        question_number = randint(1, number_up_range)
        print('Question: {}'.format(question_number), '\nYour answer: ', end='')
        user_answer = input()
        correct_answer = even_correct_answer(question_number)
        count_answers = comparing_answers(correct_answer, user_answer,
                                          count_answers, ANSWERS_TO_WIN,
                                          user_name)
        count_answers += 1
    return count_answers
