# 9461 파도반 수열

"""
2
6
12

"""

n = int(input())

padovan_dict = dict()
padovan_dict[1] = 1
padovan_dict[2] = 1
padovan_dict[3] = 1
padovan_dict[4] = 2
padovan_dict[5] = 2

max_padovan = 5

def padovan(number):

    global max_padovan

    if number in padovan_dict:
        return padovan_dict[number]

    while max_padovan < number:
        max_padovan += 1
        padovan_dict[max_padovan] = padovan_dict[max_padovan-1] + padovan_dict[max_padovan-5]

    max_padovan = number
    return padovan_dict[number]



for _ in range(n):
    wanted = int(input())
    print(padovan(wanted))