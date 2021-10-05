"""Script of game if_even."""

from random import randint
from brain_game.scripts import brain_games
from brain_game.games.check_user_answer import check_answer
from brain_game.games.correct_answers import even_correct_answer


def main():
    """Do the game and returns on screen the result of game of user."""
    user_name = brain_games.main()
    count_answers = 0
    answers_to_win = 3
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while count_answers < answers_to_win:
        number_up_range = 1000000
        question_number = randint(1, number_up_range)
        print('Question: {}'.format(question_number), '\nYour answer: ', end='')
        user_answer = input()
        correct_answer = even_correct_answer(question_number)
        count_answers = check_answer(correct_answer, user_answer,
                                     count_answers, answers_to_win, user_name)
        count_answers += 1
    if count_answers == answers_to_win:
        # если игрок ошибкся, фукнция check_user_answer
        # вернёт максимальное значение, а в
        # последнем шаге while мы это значение увеличим
        print('Congratulations, {}!'.format(user_name))


if __name__ == '__main__':
    main()
