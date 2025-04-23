N = int(input())
X = list()
Y = list()

for i in range(N):
    A, B = map(int, input().split())
    X.append(A)
    Y.append(B)

R = max(X) - min(X)
H = max(Y) - min(Y)
print(R*H)
