'''
a program that raises a a number by another number
'''


def raised_to(x, y):
    """ Brute Force
    take x multi by itself y times 
    time: O(2^n)
    """
    """ recursive algorithm
    even: [(x^y/2)^2]
    odd: [x*(x^y/2)^2]
    time: O(n)
    """
    result, power = 1.0, y
    if y < 0:
        power, x = -power, 1.0 / x
    print("\t\t\tRaising", x, "to the power of", power, '=', bin(power))
    while power:
        print('\tPower is', power)
        if power & 1:  # even or odd
            print('that is odd so lets multiply our result by', x)
            result *= x
            print('\tResult is now', result)
        else:
            print('That is even')
        x, power = x * x, power >> 1
        print('we can simplify this by setting x to x^2 =', x,
              'and raising that to the power of', power, '=', bin(power))
    print('Oh wait looks like we are done! The result is', result)
    return result


if __name__ == "__main__":

    raised_to(13, 14)
