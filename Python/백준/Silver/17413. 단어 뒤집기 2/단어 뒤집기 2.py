S = input()
length = len(S)
stack = []

i = 0
while i < length:
    if S[i] == '<':
        while stack:
            print(stack.pop(), end='')
        
        while i < length and S[i] != '>':
            print(S[i], end='')
            i += 1
        print('>', end='') 
        i += 1 

    elif S[i] == ' ':
        while stack:
            print(stack.pop(), end='')
        print(' ', end='') 
        i += 1

    else:
        stack.append(S[i])
        i += 1

while stack:
    print(stack.pop(), end='')