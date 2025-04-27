N, K = map(int, input().split())
L = list(map(int, input().split()))

L = sorted(L)
L = list(reversed(L))

print(L[K-1])
