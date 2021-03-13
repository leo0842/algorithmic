"""
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(
"""


n = int(input())

for _ in range(n):

    parenthesis_string = list(input().strip())

    cnt = 0
    answer = ""

    while parenthesis_string:
        parenthesis_char = parenthesis_string.pop(0)

        if parenthesis_char == "(":
            cnt += 1
        else:
            cnt -= 1

        if cnt < 0:

            answer = "NO"
            break

    if cnt == 0:
        answer = "YES"
    else:
        answer = "NO"
    print(answer)
