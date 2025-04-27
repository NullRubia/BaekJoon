N = int(input())
S = 0
A = N//5

if A >= 2:
    if (N%5) == 0:
        S = A
    elif (N%5) == 1:
        S = A+1
    elif (N%5) == 2:
        S = A+2
    elif (N%5) == 3:
        S = A+1
    elif (N%5) == 4:
        S = A+2
    else:
        S = -1
elif A >= 1:
    if (N%5) == 0:
        S = A
    elif (N%5) == 1:
        S = A+1
    elif (N%5) == 3:
        S = A+1
    elif (N%5) == 4:
        S = A+2
    else:
        S = -1
else:
    if (N%3) == 0:
        S = (N//3)
    else:
        S = -1

print(S)
