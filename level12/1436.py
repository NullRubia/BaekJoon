N = int(input())
S = 0
M = 666

while True:
    if "666" in str(M):
        S += 1
    if S == N:
        print(M)
        break
    M += 1
