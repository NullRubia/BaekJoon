T = int(input())
for i in range(T) :
    R, S = input().split()
    R = int(R)
    S = str(S)
    A = len(S)
    for j in range(A) :
        print(S[j]*R, end="")
    print()
