import random
import functools
import string


def baseto(s, base_i, base_f):
    def from_base(num, base):
        return ('' if num == 0 else
                from_base(num // base, base) + string.hexdigits[num % base].upper())

    is_neg = s[0] == '-'
    num = functools.reduce(
        lambda x, c: x * base_i + string.hexdigits.index(c.lower()),
        s[is_neg:], 0)
    return ('-' if is_neg else '') + ('0' if num == 0 else
                                      from_base(num, base_f))


if __name__ == "__main__":
    s = str(random.randint(10, 100))
    b1 = random.randint(3, 17)
    b2 = random.randint(3, 17)
    print(baseto(s, b1, b2))
