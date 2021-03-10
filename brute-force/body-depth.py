"""
5
55 185
58 183
88 186
60 175
46 155
"""

n = int(input())

people = []
weight = 0
height = 1

for _ in range(n):
    people.append(list(map(int, input().split())))

number_of_people = len(people)
rank = [1] * number_of_people

for i in range(number_of_people):
    for j in range(i, number_of_people):
        people_i_weight = people[i][weight]
        people_j_weight = people[j][weight]
        people_i_height = people[i][height]
        people_j_height = people[j][height]

        if people_i_weight != people_j_weight and people_i_height != people_j_height:

            i_more_weight = (people_i_weight > people_j_weight)
            i_more_height = (people_i_height > people_j_height)


            if i_more_weight and i_more_height:
                rank[j] += 1
            elif (not i_more_weight) and (not i_more_height):
                rank[i] += 1

print(" ".join(map(str, rank)))