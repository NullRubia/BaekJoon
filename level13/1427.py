N = str(input())
N = sorted(N)

N = list(reversed(N))

for i in range(len(N)):
    print(N[i], end="")
