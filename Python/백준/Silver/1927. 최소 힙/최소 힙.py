import sys
import heapq

input = sys.stdin.readline
my_heap = []

N = int(input())
for _ in range(N):
    data = int(input())  # 이 부분의 앞쪽 공백이 문제였습니다.
    if data == 0:
        if not my_heap:
            print(0)
        else:
            print(heapq.heappop(my_heap))
    else:
        heapq.heappush(my_heap, data)