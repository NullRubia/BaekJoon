import sys
N, M = map(int, sys.stdin.readline().split())
L = list()
for x in range(N) :
    L.append(x+1)
    x = x+1

for y in range(M) :
    i, j = map(int, sys.stdin.readline().split())
    a = L[i-1]
    L[i-1] = L[j-1]
    L[j-1] = a
    y = y+1

for z in range(N) :
    print(L[z], end=" ")
