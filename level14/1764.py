N, M = map(int, input().split())

H_name = set()
S_name = set()

for i in range(N):
    A = input()
    H_name.add(A)

for j in range(M):
    A = input()
    S_name.add(A)


L = list(H_name & S_name)
L.sort()

print(len(L))

for o in L:
    print(o)
