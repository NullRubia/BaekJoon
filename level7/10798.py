L = list()
for i in range(5):
    R = list(str(input()))
    L.append(R)

for j in range(15):
    for k in range(5):
        if j < len(L[k]):
            A = L[k][j]
            print(A, end="")
        else:
            pass
