N = int(input())
L = list()

for i in range(N):
    A = str(input())
    L.append(A)

L = set(L) #중복값 제거
L = list(L) # 다시 리스트로 변환

L.sort() #알파벳 순으로 정렬
L.sort(key = len) # 길이 순으로 정렬

for i in L:
    print(i)
