import math
a=int(input())
b=int(input())
c=int(input())
def solution():
    d=b*b-(4*a*c)
    sqrt=math.sqrt(abs(d))
    if d>0:
        root1=-b+sqrt/(2*a)
        root2=-b-sqrt/(2*a)
        print(root1)
        print(root2)
    elif d==0:
        root=-b/(2*a)
        print(root)
        print(root)
    else:
        real=-b/(2*a)
        root1=f"{real}+i{sqrt:.2f}"
        root2=f"{real}-i{sqrt:.2f}"
        print(root1)
        print(root2)
solution()
