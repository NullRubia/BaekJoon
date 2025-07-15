import sys
input = sys.stdin.readline

N = int(input())
company = {}
for _ in range(N):
    A, state = input().rstrip().split()
    if state == 'enter':
        company[A] = True
    else:
        del company[A]

print("\n".join(sorted(company.keys(), reverse=True)))
