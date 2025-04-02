N = int(input())
G = N
for i in range(N):
    A = str(input())
    B = len(A)
    for j in range(B-1) :
        if A[j] == A[j+1] :
            pass
        elif A[j] in A[j+1:] :
            G = G-1
            break
print(G)
