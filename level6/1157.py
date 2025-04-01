A = str(input().upper())
B = list(set(A))
S = list()
for i in B :
    C = A.count(i)
    S.append(C)

M = max(S)
IN = S.index(M)
if S.count(M) >= 2 :
    print("?")
else :
    print(B[IN])
