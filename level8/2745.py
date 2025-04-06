L = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = map(str, input().split())
B = int(B)
N = N[::-1]
X = len(N)
A = 0
for i in range(X):
    A += (B**i)*(L.index(N[i]))

print(A)
