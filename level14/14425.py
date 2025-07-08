N, M = map(int, input().split())
A = list()
B = list()
count = 0

for i in range(N):
    word = input()
    A.append(word)

for j in range(M):
    word2 = input()
    if word2 in A:
        count += 1

print(count)
