'''
Codewars problem: 

You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.

Examples:(Input --> Output)

121 --> 144
625 --> 676
114 --> -1 since 114 is not a perfect square

'''

import math
sq1 = 728


def find_next_square(sq):
    square = math.sqrt(sq)
    next_perfect_square = 0
    if ((square * 10) % 10 == 0):
        square += 1
        next_perfect_square = square ** 2
        return int(next_perfect_square)
    else:
        return -1

print(find_next_square(7399))

