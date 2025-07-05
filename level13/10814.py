N = int(input())
L = list()

for i in range(N):
    A, B = input().split()
    C = [int(A), B]
    L.append(C)

L.sort(key = lambda x : x[0]) # 나이만 비교하여 정렬

for i in L:
    print(i[0], i[1])
