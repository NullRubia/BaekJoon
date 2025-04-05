L = list()
A = list()
for i in range(9):
    C = list(map(int, input().split()))
    L.append(C)
for j in range(9):
    for k in range(9):
        B = L[j][k]
        A.append(B)
M = max(A)

for k in range(9):
    for q in range(9):
        if L[k][q] == M :
            X = k+1
            Y = q+1
        else:
            pass

print(M)
print(X, Y)
