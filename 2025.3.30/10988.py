A = str(input())
L = len(A)
for i in range(L) :
    if A[i] == A[-1-i] :
        pass
    else :
        print(0)
        exit(0)
print(1)
