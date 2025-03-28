H, M = input().split()
H = int(H)
M = int(M)
C = int(input())
if C+M >= 60 :
    H = H+((C+M)//60)
    if H >= 24 :
        H = H-24
    M = (C+M)%60
    print(H, M)
else :
    M = C+M
    print(H, M)
