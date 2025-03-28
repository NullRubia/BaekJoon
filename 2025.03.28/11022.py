import sys
T = int(sys.stdin.readline())
i = 0
while i < T :
    i = i+1
    A, B = map(int, sys.stdin.readline().split())
    s = i
    s = str(s)
    print("Case #"+s+":", A, "+", B, "=", A+B)
