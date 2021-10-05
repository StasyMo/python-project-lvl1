"""Script of game calculator."""

from random import choice, randint
from brain_game.scripts import brain_games
from brain_game.games.check_user_answer import check_answer
from brain_game.games.correct_answers import calc_correct_answer


def main():
    """Do the game and returns on screen the result of game of user."""
    user_name = brain_games.main()
    count_answers = 0
    answers_to_win = 3
    print('What is the result of the expression?')
    while count_answers < answers_to_win:
        number_up_range = 100
        calc_number1 = randint(1, number_up_range)
        calc_number2 = randint(1, number_up_range)
        math_operator = choice(['+', '-', '*'])
        print('Question: {0} {1} {2}'.format(calc_number1,
                                             math_operator, calc_number2),
              'Your answer: ', end='')
        user_answer = input()
        try:
            user_answer = int(user_answer)
        except ValueError:
            return print("The answer might be a number, but '{0}' "
                         "is not a number ;(. \n Let's try again, "
                         "{1}!".format(user_answer, user_name))
        correct_answer = calc_correct_answer(calc_number1,
                                             calc_number2, math_operator)
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
