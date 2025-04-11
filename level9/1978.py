N = int(input())
L = list(map(int, input().split()))
count = 0
for i in range(len(L)):
    P = list()
    A = L[i]
    for j in range(1, A+1):
        if A%j == 0:
            P.append(j)
    if len(P) == 2:
        count += 1
print(count)
