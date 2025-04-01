N = int(input())
M = N-1
for i in range(N) :
    print(" "*(N-(i+1)) + "*"*(2*(i+1)-1))
for j in range(M) :
    print(" "*(j+1) + "*"*((2*N-1)-(2*(j+1))))
