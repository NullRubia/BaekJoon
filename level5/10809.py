S = str(input())
A = 97
for i in range(26) :
    B = chr(A)
    A = A+1
    print(S.find(str(B)), end= " ")
