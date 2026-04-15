import sys
input = sys.stdin.readline
T = int(input()) 

for i in range(T):
    stack = []
    bracket = input()
    
    for j in bracket: 
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else: 
                stack.append(j)
                break
            
    if not stack:
        print("YES")
    else:
        print("NO")