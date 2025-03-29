import sys
L = list()
for x in range(30) :
    L.append(x+1)

for y in range(28) :
    n = int(sys.stdin.readline())
    L.remove(n)

print(min(L))
print(max(L))
