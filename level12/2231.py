N = int(input())

for i in range(1, N+1):
    A = list(map(int, str(i)))
    S = sum(A) + i
    if S == N:
        print(i)
        break
    elif i == N:
        print(0)
