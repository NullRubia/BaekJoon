import sys

N = int(sys.stdin.readline())

L = [0] * 10001

for i in range(N):
    A = int(sys.stdin.readline())
    L[A] += 1

for j in range(10001):
    if L[j] != 0:
        for k in range(L[j]):
            print(j)
