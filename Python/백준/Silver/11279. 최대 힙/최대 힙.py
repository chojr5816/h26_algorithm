import sys
import heapq

input = sys.stdin.readline

my_heap = []

line = input().strip()
if line:
    N = int(line)
    for _ in range(N):
        data_line = input().strip()
        if not data_line:
            continue
        data = int(data_line)
        
        if data == 0:
            if not my_heap:
                print(0)
            else:
                # 뺄 때 다시 마이너스를 붙여서 원래 양수 값으로 출력
                print(-heapq.heappop(my_heap))
        else:
            # 넣을 때 마이너스를 붙여서 넣음 (큰 값이 가장 작아지게 함)
            heapq.heappush(my_heap, -data)