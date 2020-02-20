import random
import functools
import string


def int2str(x):
    # neg check
    is_neg = False
    if x < 0:
        x, is_neg = -x, True

    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break
    return ('-'if is_neg else '') + ''.join(reversed(s))


def str2int(s):
    return functools.reduce(
        lambda running_sum, c: running_sum * 10 + string.digits.index(c),
        s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)


if __name__ == "__main__":
    s = str(random.randint(100, 1000000))
    if (int2str(str2int(s)) == s):
        print(s)
