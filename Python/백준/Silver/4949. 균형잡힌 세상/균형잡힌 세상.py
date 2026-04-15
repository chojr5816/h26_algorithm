while True:
    str = input()
    stack = []
    if str == ".": 
        break

    isGoodWord = 'yes'

    for word in str: 
        if word in ['[', '(']: 
            stack.append(word)
        
        elif word == ']':
            if not stack or stack.pop() != '[':
                isGoodWord = 'no'
                break

        elif word == ')':
            if not stack or stack.pop() != '(':
                isGoodWord = 'no'
                break

    if stack:
        isGoodWord = 'no'
    
    print(isGoodWord)