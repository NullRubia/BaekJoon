import sys
N, M = map(int, sys.stdin.readline().split())
P = dict()
num = dict()
for i in range(1, N+1):
    A = sys.stdin.readline().strip()
    P[i] = A
    num[A] = i

for i in range(M):
    find = sys.stdin.readline().strip()
    if find[0].isalpha():
        print(num[find])
    else:
        print(P[int(find)])
