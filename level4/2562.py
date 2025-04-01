import sys
L = list()
i = 0
while i < 9 :
    A = int(sys.stdin.readline())
    L.append(A)
    i = i+1
print(max(L))
print(L.index(max(L))+1)
