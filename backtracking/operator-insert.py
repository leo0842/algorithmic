"""
6
1 2 3 4 5 6
2 1 1 1

"""

n = int(input())

numbers = list(map(int, input().split()))

operators = list(map(int,input().split()))

operators_dict = dict()

operators_dict[0] = "+"
operators_dict[1] = "-"
operators_dict[2] = "*"
operators_dict[3] = "//"

max_num = float('-inf')
min_num = float('inf')

def operation(ops, num1, num2):

    if ops == "+":
        return num1 + num2
    elif ops == "-":
        return num1 - num2
    elif ops == "*":
        return num1 * num2
    else:
        if num1 < 0:
            return -(-num1//num2)
        else:
            return num1//num2

cnt = 0
def find_ops(num, idx, operator_list):
    
    global numbers, max_num, min_num, cnt

    cnt += 1


    if idx == len(numbers)-1:
        max_num = max(num, max_num)
        min_num = min(num, min_num)

        return

    for i in range(len(operator_list)):
        if operator_list[i]:
            temp_list = operator_list[:]
            temp_list[i] -= 1

            next_num = operation(operators_dict[i], num, numbers[idx+1])

            find_ops(next_num, idx+1, temp_list)


find_ops(numbers[0], 0, operators)

print(max_num)
print(min_num)
print(cnt)

print("======================================================================================")
"""
6
1 2 3 4 5 6
2 1 1 1

"""

from itertools import permutations as P

n = int(input())

numbers = list(map(int, input().split()))

operator_count = list(map(int,input().split()))

operators = []

raw_operators = ["+","-","*","/"]

for idx, op in enumerate(operator_count):
    for i in range(op):
        operators.append(raw_operators[idx])

operator_permutations = set(P(operators))
cnt = 0
max_num = float('-inf')
min_num = float('inf')
for p in operator_permutations:
    temp_operation = numbers[0]
    for idx, op in enumerate(p):
        cnt += 1
        next_number = numbers[idx+1]
        if op == "+":
            temp_operation += next_number
        elif op == "-":
            temp_operation -= next_number
        elif op == "*":
            temp_operation *= next_number
        else:
            if temp_operation < 0:
                temp_operation = -((-temp_operation)//next_number)
            else:
                temp_operation = int(temp_operation//next_number)

    if temp_operation > max_num:
        max_num = temp_operation
    if temp_operation < min_num:
        min_num = temp_operation

print(max_num)
print(min_num)


print(cnt)