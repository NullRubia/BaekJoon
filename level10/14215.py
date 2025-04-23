A, B, C = map(int, input().split())
L = max(A,B,C)

if L >= (A+B+C)-L:
    L = (A+B+C)-L-1
    print((2*L)+1)
else:
    print(A+B+C)
