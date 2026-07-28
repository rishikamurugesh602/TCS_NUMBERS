
a=int(input())
b=int(input())
res=[]
def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        return True
    else:
        return False
def solution():
    for i in range(a,b+1):
        if prime(i):
            res.append(i)
    return res
print(solution())
    
