N, M, K = input().split(" ")

N = int(N)
M = int(M)
K = int(K)

n = K // M
m = K % M

print(n, m)