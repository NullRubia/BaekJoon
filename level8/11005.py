C = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str(C)
N, B = map(int, input().split())
L = list()
M = list()
while True:
    if N == 0 :
        break
    else:
        A = N%B
        L.append(A)
        N = N//B

L = L[::-1]
X = len(L)
for i in range(X):
    L[i] = C[L[i]]

for i in range(X):
    print(L[i], end="")
