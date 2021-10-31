from brain_game.scripts import brain_games
import prompt


def run_game(rules, get_question_and_answer):
    user_name = brain_games.main()
    print(rules)
    count_answers = 0
    ANSWERS_TO_WIN = 3
    while count_answers < ANSWERS_TO_WIN:
        question, correct_answer = get_question_and_answer()
        print('Question: {}'.format(question))
        user_answer = prompt.string('Your answer: ')
        if correct_answer == user_answer:
            print('Correct!')
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'. "
                  "\nLet's try again, "
                  "{2}!".format(user_answer, correct_answer, user_name))
            count_answers = ANSWERS_TO_WIN
        count_answers += 1
    if count_answers == ANSWERS_TO_WIN:
        print('Congratulations, {}!'.format(user_name))
