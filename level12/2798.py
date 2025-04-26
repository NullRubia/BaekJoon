N, M = map(int,input().split())
L = list(map(int,input().split()))
B = list()
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            A =  L[i] + L[j] + L[k]
            if A > M:
                continue
            else:
                B.append(A)

print(max(B))
