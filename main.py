import pyperclip
import random
import string
import sys
DEFAULT_PASS_LEN = 31


def main(N: int) -> str:
    possible = list(string.ascii_letters)
    possible.extend(list(string.punctuation))
    possible.extend(list(string.digits))
    gen: random.SystemRandom = random.SystemRandom()
    P: str = ""
    i = 0
    while i < N:
        P += gen.choice(possible)
        i += 1
    pyperclip.copy(P)
    return P


if __name__ == '__main__':
    N = DEFAULT_PASS_LEN
    if len(sys.argv) > 1:
        if sys.argv[1].isdigit():
            N = int(sys.argv[1])
            if N <= 0:
                N = DEFAULT_PASS_LEN
    print(main(N))
    exit(0)
