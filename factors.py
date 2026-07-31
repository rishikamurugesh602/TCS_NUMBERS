import math
n = int(input())

def factor(n):
    res=[]
    for i in range(1,int(math.sqrt(n)+1)):
        if n%i==0:
            res.append(i)
            if i!=n//i:
                res.append(n//i)
    return res
print(factor(n))
        
