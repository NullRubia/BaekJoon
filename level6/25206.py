S = 0
V = 0
H = 0
for i in range(20):
    A, B, C = input().split()
    B = float(B)
    H = H+B
    if C == "P" :
        H = H-B
        V = 0
    elif C == "A+" :
        V = 4.5
    elif C == "A0" :
        V = 4.0
    elif C == "B+" :
        V = 3.5
    elif C == "B0" :
        V = 3.0
    elif C == "C+" :
        V = 2.5
    elif C == "C0" :
        V = 2.0
    elif C == "D+" :
        V = 1.5
    elif C == "D0" :
        V = 1.0
    else :
        V = 0
    S = S + V*B

Avg = S/H
print(Avg)
