L=list()
while True:
    N = int(input())
    if N == -1:
        break
    for i in range(1, N+1):
        if N%i == 0:
            L.append(i)
    print(N, end = " ")
    A = len(L)
    S = 0
    for j in range(A-1):
        S += L[j]
    if N == S:
        print("=", end = " ")
        for k in range(A-2):
            print(L[k], end = " + ")
        print(L[A-2])
        L = list()
    else:
        print("is NOT perfect.")
        L = list()
