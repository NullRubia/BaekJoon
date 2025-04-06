L = [[0 for i in range(100)] for j in range(100)]

N = int(input())

for q in range(N):
    A, B = map(int, input().split())
    
    for w in range(A, A+10):
        for e in range(B, B+10):
            L[w][e] = 1

M = 0
for r in range(100):
    M += L[r].count(1)

print(M)
