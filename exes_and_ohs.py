'''
Codewars problem:

Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
'''

s = 'OoXX'

def xo(s):
    x = 0
    o = 0
    s = s.upper()
    for l in s:
        if l == 'X':
            x += 1
        elif l == 'O':
            o += 1
    if x == o:
        return True
    elif x == 0 and o == 0:
        return True
    else:
        return False

print(xo(s))