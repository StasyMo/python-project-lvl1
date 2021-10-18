from brain_game.scripts import brain_games
from brain_game.games.gcd_module import gcd_game
from brain_game.games.even_module import even_game
from brain_game.games.calc_module import calc_game
from brain_game.games.progression_module import progression_game
from brain_game.games.prime_module import prime_game


def engine_of_game(name_of_game):
    user_name = brain_games.main()
    count_answers = 0
    ANSWERS_TO_WIN = 3
    if name_of_game == 'gcd':
        result_of_game = gcd_game(user_name, count_answers,
                                  ANSWERS_TO_WIN)
    if name_of_game == 'even':
        result_of_game = even_game(user_name, count_answers,
                                   ANSWERS_TO_WIN)
    if name_of_game == 'calc':
        result_of_game = calc_game(user_name, count_answers,
                                   ANSWERS_TO_WIN)
    if name_of_game == 'progression':
        result_of_game = progression_game(user_name, count_answers,
                                          ANSWERS_TO_WIN)
    if name_of_game == 'prime':
        result_of_game = prime_game(user_name, count_answers,
                                    ANSWERS_TO_WIN)

    if result_of_game == 'win':
        print('Congratulations, {}!'.format(user_name))
