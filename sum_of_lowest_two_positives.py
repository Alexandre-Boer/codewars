'''
Codewars problem:

Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.
'''


def sum_two_smallest_numbers(numbers):
    for n in numbers:
        sum = 0
        if isinstance(n, int):
            numbers.sort()
            sum = numbers[0] + numbers[1]
        else:
            pass
    return sum
    
numbers = [2, 4, 59, 32, 25, 44, 1, 3.3]

print(sum_two_smallest_numbers(numbers))