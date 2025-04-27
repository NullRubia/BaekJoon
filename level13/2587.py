L = list()
S = 0
for i in range(5):
    A = int(input())
    L.append(A)
    S += A

L = sorted(L)
Avg = S//5

print(Avg)
print(L[2])
