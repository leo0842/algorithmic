"""
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10

"""

import sys

sys.setrecursionlimit(10000)

row, col = map(int, input().split())

def visitable(x, y):
    return (0 <= x < row) and (0 <= y < col)

map_matrix = []
for _ in range(row):
    map_matrix.append(list(map(int, input().split())))

visit_matrix = [[-1] * col for _ in range(row)]

directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]

def downhill(x, y):
    if x == 0 and y == 0:
        return 1
    
    if visit_matrix[x][y] == -1:
        visit_matrix[x][y] = 0
        for dx, dy in directions:
            adjacent_x, adjacent_y = x + dx, y + dy
            if visitable(adjacent_x, adjacent_y):
                if map_matrix[x][y] < map_matrix[adjacent_x][adjacent_y]:
                    visit_matrix[x][y] += downhill(adjacent_x, adjacent_y)
    
    return visit_matrix[x][y]

print(downhill(row-1, col-1))


