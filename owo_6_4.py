
def owo(s):
    for i in range(len(s)):
        if s[i] == 'r' or s[i] == 'R' or s[i] == 'l' or s[i] == 'L':
            s[i] = 'w'
    print(s)


if __name__ == "__main__":
    s = 'a,a,a,b,b,b,r,r,r,f,l,l,l,f,l,b'.split(',')
    owo(s)
