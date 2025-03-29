import sys
N, M = map(int, sys.stdin.readline().split())
L = list()
a = 0
b = 0
c = 0
while a < N :
    L.append(0)
    a = a+1
    
while b < M :
    i, j, k = map(int, sys.stdin.readline().split())
    while i < j+1 :
        del L[i-1]
        L.insert(i-1, k)
        i = i+1
    b = b+1
while c < N :
    print(L[c], end=" ")
    c = c+1
