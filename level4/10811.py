import sys
N, M = map(int, sys.stdin.readline().split())
L = list()
for x in range(N) :
    L.append(x+1)


for y in range(M) :
    i, j = map(int, sys.stdin.readline().split())
    A = j-(i-1)
    for z in range(A//2) :
        a = L[i-1]
        L[i-1] = L[j-1]
        L[j-1] = a
        i = i+1
        j = j-1
        z = z+1
    y = y+1
for b in range(N) :
    print(L[b], end=" ")
    b = b+1
