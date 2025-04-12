M = int(input())
N = int(input())
S = list()
for i in range(M, N+1):
    L = list()
    for j in range(1, i+1):
        if i%j == 0:
            L.append(j)
    if len(L) == 2:
        S.append(i)

if len(S) < 1:
    print(-1)
else:
    print(sum(S))
    print(S[0])
