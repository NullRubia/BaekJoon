Q, D, N, P = int(25), int(10), int(5), int(1)
T = int(input())
for i in range(T):
    C = int(input())
    Qn = C//Q
    C = C%Q
    Dn = C//D
    C = C%D
    Nn = C//N
    Pn = C%N
    print(Qn, Dn, Nn, Pn)
