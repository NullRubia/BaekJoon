T = str(input())
if T[0] == " " and T[-1] == " " :
    print(T.count(" ")-1)
elif T[0] == " " or T[-1] == " " :
    print(T.count(" "))
else :
    print(T.count(" ")+1)
