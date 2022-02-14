'''
Codewars problem: 

This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
'''

def accum(s):
    # storage the number position of the letter
    number = 0
    # storage a list of strings
    temp_string = []
    # variable to storage the index of each word in temp_string
    i = 0
    # checking each character in s
    for l in s:
        #checking if the character is [A-z]
        if l.isalpha():
            number += 1
            temp_string.append(l * number)
        else:
            pass
    # Checking each word in temp_string and capitalize them
    for w in temp_string:
        temp_string[i] = w.capitalize()
        i = i + 1
    new_string = "-".join(temp_string)
    return new_string

print(accum('awsde23s'))