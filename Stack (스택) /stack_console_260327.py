stack = []
MAX = 5

while True:
    print("\n[ 정수형 스택 연산 실습 (용량 5) ]")
    print("==================================================")
    print("  1.Push    2.Pop    3.Peek    0.Exit")
    print("==================================================")
    
    a = input("> 메뉴 선택 : ")

    if a == '1':
        if len(stack) < MAX:
            data = input("> 데이터 입력 : ")
            if data.isdigit(): 
                stack.append(int(data))  # 스택의 맨 위 추가
        else:
            print("> Stack이 차 있어서 더 이상 추가할 수 없습니다.")

    elif a == '2':
        if stack:
            print(f"> 가져온 데이터 : {stack.pop()}")
        else:
            print("> Stack이 비어 있습니다.")

    elif a == '3':
        if stack:
            print(f"> 확인된 데이터 : {stack[-1]}")
        else:
            print("> Stack이 비어 있습니다.")

    elif a == '0':
        print("[ 정수형 스택 연산 실습 종료]")
        break

    # 결과 출력
    print(f"> 현재 스택 상태  {stack}")
