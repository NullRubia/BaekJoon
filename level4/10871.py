N, X = map(int,input().split())
A = list(map(int, input().split()))
i = 0
S = ""
while i < N :
    if A[i] < X :
        S = S+str(A[i])+" "
    i = i+1
print(S)
