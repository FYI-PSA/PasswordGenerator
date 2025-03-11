import pyperclip
import random
import string
import sys
DEFAULT_PASS_LEN = 31


def passwordGen(N: int) -> str:
    possible = []
    possible.extend(list(string.ascii_lowercase))
    possible.extend(list(string.ascii_uppercase))
    possible.extend(list(string.digits))
    possible.extend(list(string.punctuation))
    OSrand: random.SystemRandom = random.SystemRandom()
    P: str = ""
    i: int = 0
    while i < N:
        P += OSrand.choice(possible)
        i += 1
    return P


if __name__ == '__main__':
    N: int = DEFAULT_PASS_LEN
    if len(sys.argv) > 1:
        if sys.argv[1].isdigit():
            N = int(sys.argv[1])
            if N <= 0:
                N = DEFAULT_PASS_LEN
    P: str = passwordGen(N)
    print(P)
    pyperclip.copy(P)
    exit(0)
