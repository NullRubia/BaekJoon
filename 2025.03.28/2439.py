N = int(input())
B = " "
star = "*"
i = 0
while i < N :
    i = i+1
    print((B*(N-i))+star)
    star = star + "*"
