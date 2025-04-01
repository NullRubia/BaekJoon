X = int(input())
N = int(input())
i = 0
cost = 0
while i < N :
    i = i+1
    a, b = map(int, input().split())
    c = a*b
    cost = cost+c

if X == cost :
    print("Yes")
else :
    print("No")
