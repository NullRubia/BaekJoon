x, y, w, h = map(int, input().split())
A = w-x
B = h-y
L = [x, y, A, B]
print(min(L))
