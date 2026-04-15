M = 1234567891
r = 31

L = int(input())
A = input().strip()

h = 0
for i in range(L):
    h += (ord(A[i]) - ord('a') + 1) * r ** i

print(h % M)