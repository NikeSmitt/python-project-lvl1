import random
import brain_games.game_loop


GAME_MESSAGE = 'Find the greatest common divisor of given numbers.'
TOP = 100
BOTTOM = 1


def get_gcd(a, b):
    if a % b == 0:
        return b
    return get_gcd(b, a % b)


def gcd_game():
    a = random.randint(BOTTOM, TOP)
    b = random.randint(BOTTOM, TOP)
    right_answer = get_gcd(a, b)
    return f"{a} {b}", str(right_answer)


def main():
    brain_games.game_loop.main(GAME_MESSAGE, gcd_game)


if __name__ == "__main__":
    main()
