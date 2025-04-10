N, K = map(int, input().split())
L=list()
for i in range(1, N+1):
    if N%i == 0:
        L.append(i)
A = len(L)
if K <= A:
    print(L[K-1])
else:
    print("0")
