from brain_game.cli import welcome_user
import prompt


ROUNDS_COUNT = 3


def run_game(rules, get_question_and_answer):
    print('Welcome to the Brain Games!')
    user_name = welcome_user()
    print(rules)
    for _ in range(ROUNDS_COUNT):
        question, correct_answer = get_question_and_answer()
        print('Question: {}'.format(question))
        user_answer = prompt.string('Your answer: ')
        if correct_answer == user_answer:
            print('Correct!')
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'. "
                  "\nLet's try again, "
                  "{2}!".format(user_answer, correct_answer, user_name))
            return
    print('Congratulations, {}!'.format(user_name))
