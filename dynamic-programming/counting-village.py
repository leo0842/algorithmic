# 2667 단지번호붙이기

"""
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

"""
n = int(input())

houses = []

for _ in range(n):
    a = list(map(int,list(input())))

    houses.append(a)


def visitable(row, col):
    return 0 <= row < n and 0 <= col < n

visited = [[0] * n for _ in range(n)]

directions = [[0,1],[0,-1],[1,0],[-1,0]]

number_of_house = 0

def find_village(row, col):

    global directions, number_of_house
    
    if not visitable(row, col):
        return

    if not houses[row][col]:
        return

    if visited[row][col]:
        return

    visited[row][col] = 1

    number_of_house += 1

    for dx, dy in directions:

        find_village(dx+row, dy+col)


answer = []
for row in range(n):
    for col in range(n):

        if houses[row][col]:
            number_of_house = 0
            find_village(row, col)
            if number_of_house:
                answer.append(number_of_house)

print(len(answer))
answer = sorted(answer)
for i in answer:
    print(i)
