N = int(input())
L = list()
for i in range(N):
    a,b = map(int,input().split())
    L.append((a,b))
L = sorted(L)
for j in range(N):
    print(L[j][0], L[j][1])
