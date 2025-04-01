H, M = input().split()
H = int(H)
M = int(M)
S = M-45
if M < 45 :
    if H < 1 :
        H = 24-1
    else :
        H = H-1
    M = 60+S
    print(H, M)
else :
    M = M-45
    print(H, M)
