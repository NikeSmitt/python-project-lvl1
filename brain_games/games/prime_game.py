import random
import brain_games.game_loop

GAME_MESSAGE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
TOP = 100
BOTTOM = 10


def is_prime(value):
    dev = 2
    while dev < value ** 0.5:
        if value % dev == 0:
            return False
        dev += 1
    return True


def prime_game():
    question = random.randint(BOTTOM, TOP)
    right_answer = 'yes' if is_prime(question) else 'no'
    return f'{question}', right_answer


def main():
    brain_games.game_loop.main(GAME_MESSAGE, prime_game)


if __name__ == "__main__":
    main()
