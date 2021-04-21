import random
import brain_games.game_loop

WELCOME_MESSAGE = 'Answer "yes" if the number is even, ' \
                  'otherwise answer "no".'

TOP = 100
BOTTOM = 1


def is_even(value) -> str:
    return "yes" if value % 2 == 0 else "no"


def even_game():
    value = random.randint(BOTTOM, TOP)
    right_answer = is_even(value)
    return value, right_answer


def main():
    brain_games.game_loop.main(WELCOME_MESSAGE, even_game)


if __name__ == "__main__":
    main()
