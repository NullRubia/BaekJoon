S = str(input())
L = len(S)
T = 0
for i in range(L) :
    A = S[i]
    A = ord(A)
    if A >= 65 and A <= 67 :
        B = 3
    elif A >= 68 and A <= 70 :
        B = 4
    elif A >= 71 and A <= 73 :
        B = 5
    elif A >= 74 and A <= 76 :
        B = 6
    elif A >= 77 and A <= 79 :
        B = 7
    elif A >= 80 and A <= 83 :
        B = 8
    elif A >= 84 and A <= 86 :
        B = 9
    elif A >= 87 and A <= 90 :
        B = 10
    T = T+B
print(T)
