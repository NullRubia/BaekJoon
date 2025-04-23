while True:
    A, B, C = map(int, input().split())
    if A == 0 and B == 0 and C == 0:
        break
    elif max(A,B,C) >= (A+B+C)-max(A,B,C):
        print("Invalid")
    elif A == B and B == C:
        print("Equilateral")
    elif A == B or A == C or B == C:
        print("Isosceles")
    else :
        print("Scalene")
