import sys
from collections import deque


N = int(sys.stdin.readline().rstrip())
array = deque([])

for i in range(N):
    command = sys.stdin.readline().rstrip().split()
    if (command[0] == "push_front"):
        array.appendleft(command[1])
    elif (command[0] == "push_back"):
        array.append(command[1])
    elif (command[0] == "pop_front"):
        if array:
            print(array.popleft())
        else:
            print("-1")
            
    elif (command[0] == "pop_back"):
        if array:
            print(array.pop())
        else:
            print("-1")
            
    elif (command[0] == "size"):
        print(len(array))

    elif (command[0] == "empty"):
        if array:
            print("0")
        else:
            print("1")
    elif (command[0] == "front"):
        if array:
            print(array[0])
        else:
            print("-1")
    else:
        if array:
            print(array[len(array) - 1])
        else:
            print("-1")