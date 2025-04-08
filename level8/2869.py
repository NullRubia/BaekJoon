A, B, V = map(int, input().split())
V = V-B
C = A-B

if V%C == 0:
    print(V//C)
else:
    print((V//C)+1)
