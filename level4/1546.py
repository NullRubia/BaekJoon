import sys
N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
A = 0
M = max(L)
for i in range(N) :
    L[i] = (L[i]/M)*100

for j in range(N) :
    A = A+L[j]
    
print(A/N)
