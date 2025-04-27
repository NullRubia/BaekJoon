import sys

N = int(sys.stdin.readline())
L = list()
for i in range(N):
    A = int(sys.stdin.readline())
    L.append(A)

L = sorted(L)

for j in range(N):
    print(L[j])
