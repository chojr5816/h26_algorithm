import sys
input = sys.stdin.readline

num_node = int(input())

# 트리 생성
tree = {}
for _ in range(num_node):
    # split()은 기본적으로 공백을 기준으로 나누므로 strip() 없이도 깔끔하게 들어옵니다.
    data, left, right = input().split()
    tree[data] = [left, right]

# 전위 순회 (Root - Left - Right)
def preorder(data):
    if data == '.':
        return
    print(data, end='') # 공백 제거
    preorder(tree[data][0])
    preorder(tree[data][1])

# 중위 순회 (Left - Root - Right)
def inorder(data):
    if data == '.':
        return
    inorder(tree[data][0])
    print(data, end='') # 공백 제거
    inorder(tree[data][1])

# 후위 순회 (Left - Right - Root)
def postorder(data):
    if data == '.':
        return
    postorder(tree[data][0])
    postorder(tree[data][1])
    print(data, end='') # 공백 제거

# 실행 및 줄바꿈
preorder('A')
print()
inorder('A')
print()
postorder('A')