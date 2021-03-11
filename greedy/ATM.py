"""
5
3 1 4 3 2

"""
import heapq

n = int(input())
people_list = list(map(int, input().split()))

heapq.heapify(people_list)

waiting_time = 0
total_waiting_time = 0
while people_list:
    waiting_time += heapq.heappop(people_list)
    total_waiting_time += waiting_time

print(total_waiting_time)
