"""
8
4
3
6
8
7
5
2
1

"""

n = int(input())

permutation = []

for _ in range(n):
    permutation.append(int(input()))

next_number = 1
stack = []
answer = []
while permutation:

    if next_number < permutation[0]:
        stack.append(next_number)
        next_number += 1
        answer.append("+")
    elif next_number == permutation[0]:
        next_number += 1
        answer.append("+")
        answer.append("-")
        permutation.pop(0)
    else:
        if stack[-1] == permutation[0]:
            answer.append("-")
            permutation.pop(0)
            stack.pop()

        else:
            break


if not permutation:
    for i in answer:
        print(i)
else:
    print("NO")

