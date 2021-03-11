"""
7
6
1 2
2 3
1 5
5 2
5 6
4 7
"""

number_of_computer = int(input())
number_of_pair = int(input())

pair_list = []

for _ in range(number_of_pair):
    pair_list.append(list(map(int, input().split())))

visited_list = []
queue_list = [1]
answer = []
while queue_list:
    worm_computer = queue_list.pop(0)
    for i in pair_list:
        if worm_computer in i:
            if i not in visited_list:
                visited_list.append(i)
                if i[0] == worm_computer:
                    queue_list.append(i[1])
                    answer.append(i[1])
                else:
                    queue_list.append(i[0])
                    answer.append(i[0])
print(len(set(answer)))


number_of_computer = int(input())
number_of_pair = int(input())

computer = dict()

for _ in range(number_of_pair):
    a, b = map(int, input().split())
    if a in computer:
        computer[a].append(b)
    else:
        computer[a] = [b]
    if b in computer:
        computer[b].append(a)
    else:
        computer[b] = [a]

visited = [1]
queue = [1]

while queue:
    worm = queue.pop(0)
    for i in computer[worm]:
        if i not in visited:
            visited.append(i)
            queue.append(i)



print(len(visited)-1)