A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)
if A == B and B == C :
    S = 10000+(A*1000)
elif A == B or A == C or B == C :
    if A == B :
        S = 1000+(A*100)
    elif A == C :
        S = 1000+(A*100)
    else :
        S = 1000+(B*100)
else :
    if A >= B and A >= C :
        S = A*100
    elif B >=A and B >= C :
        S = B*100
    else :
        S = C*100
print(S)
