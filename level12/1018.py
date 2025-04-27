N, M = map(int, input().split())
L = list()
R = list()
for i in range(N):
    L.append(str(input()))

for j in range(N-7):
    for k in range(M-7):
        W = 0 
        B = 0
        for o in range(j,j+8):
            for p in range(k,k+8):
                if (o + p) % 2 == 0:
                    if L[o][p]!='W':
                        W += 1
                    else:
                        B += 1
                else:
                    if L[o][p] != 'W':
                        B += 1
                    else:
                        W += 1
                        
        R.append(W)
        R.append(B)

print(min(R))
