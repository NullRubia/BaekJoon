N = int(input())
L = list()
for i in range(N):
    A = int(input())
    L.append(A)

L = sorted(L)

for j in range(N):
    print(L[j])
