N = int(input())
i = 1
A = 1
while True:
    if N > A:
        A = A+(6*i)
        i = i+1
    else:
        break
print(i)
