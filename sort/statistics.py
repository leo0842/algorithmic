import sys

n = int(input())

frequency_dict = dict()
number_list = []

def mean_check(number_list, n):

    return round(sum(number_list)/n)

def median_check(number_list, n):

    number_list = sorted(number_list)

    return number_list[int(n/2)]

def frequency_check(frequency_dict):

    if len(frequency_dict) == 1:

        return number_list[0]

    frequency_sorted = sorted(frequency_dict.items(), key=lambda x: (x[1], -x[0]), reverse=True)

    if frequency_sorted[0][1] != frequency_sorted[1][1]:

        return frequency_sorted[0][0]
    else:

        return frequency_sorted[1][0]
    
def range_check(number_list):

    return max(number_list) - min(number_list)

for _ in range(n):

    number = int(sys.stdin.readline())

    if number not in frequency_dict:
        frequency_dict[number] = 1
    else:
        frequency_dict[number] += 1
    
    number_list.append(number)

print(mean_check(number_list, n))
print(median_check(number_list, n))
print(frequency_check(frequency_dict))
print(range_check(number_list))
