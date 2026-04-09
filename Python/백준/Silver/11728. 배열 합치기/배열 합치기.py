size_A, size_B = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
merged_list = []

pA = pB = 0
while pA < size_A and pB < size_B:
    if A[pA] < B[pB]:
        merged_list.append(A[pA])
        pA += 1
    else:
        merged_list.append(B[pB])
        pB += 1

if pA < size_A:
    merged_list.extend(A[pA:size_A])

if pB < size_B:
    merged_list += B[pB:size_B]

print(" ".join(map(str, merged_list)))