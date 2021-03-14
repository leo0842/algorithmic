"""
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1

"""

n = int(input())

for _ in range(n):
    number_of_doc, wanted = map(int, input().split())
    queue = list(enumerate(list(map(int, input().split()))))
    cnt = 0
    find = False
    most_important = max(queue, key=lambda x: x[1])[1]

    while not find:
        first_in = queue.pop(0)
        if first_in[1] == most_important:
            cnt += 1
            if first_in[0] == wanted:
                find=True
            else:
                most_important = max(queue, key=lambda x: x[1])[1]
        else:
            queue.append(first_in)
    print(cnt)
        
