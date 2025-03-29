import sys
L = list()
for x in range(10) :
    n = int(sys.stdin.readline())
    a = n%42
    L.append(a)

L = set(L)
L = list(L)

print(len(L))
