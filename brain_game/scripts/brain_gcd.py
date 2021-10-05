"""Script of game gcd."""

from random import randint
from brain_game.scripts import brain_games
from brain_game.games.check_user_answer import check_answer
from brain_game.games.correct_answers import gcd_correct_answer


def main():
    """Do the game and returns on screen the result of game of user."""
    user_name = brain_games.main()
    count_answers = 0
    answers_to_win = 3
    print('Find the greatest common divisor of given numbers.')
    while count_answers < answers_to_win:
        number_up_range = 100
        gcd_number1 = randint(1, number_up_range)
        gcd_number2 = randint(1, number_up_range)
        print('Question: {0} {1} '.format(gcd_number1, gcd_number2),
              'Your answer: ', end='')
        user_answer = input()
        try:
            user_answer = int(user_answer)
        except ValueError:
            return print("The answer might be a number, but '{0}' "
                         "is not a number ;(. \n Let's try again, "
                         "{1}!".format(user_answer, user_name))
        correct_answer = gcd_correct_answer(gcd_number1, gcd_number2)
        count_answers = check_answer(correct_answer, user_answer, count_answers,
                                     answers_to_win, user_name)
        count_answers += 1
    if count_answers == answers_to_win:
        # если игрок ошибкся, фукнция check_user_answer
        # вернёт максимальное значение, а в
        # последнем шаге while мы это значение увеличим
        print('Congratulations, {}!'.format(user_name))


if __name__ == '__main__':
    main()