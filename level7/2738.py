N, M = map(int, input().split())
A = list()
B = list()
for i in range(N):
    LA = list(map(int, input().split()))
    A.append(LA)
for j in range(N):
    LB = list(map(int, input().split()))
    B.append(LB)

for r in range(N):
    for c in range(M):
        H = A[r][c] + B[r][c]
        print(H, end=" ")
    print()
