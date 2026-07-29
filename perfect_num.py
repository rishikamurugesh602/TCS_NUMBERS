n=int(input())
import math
def solution():
    res=[]
    summ=0
    for i in range(1,n):
        if n==1:
           return False
        summ=1
        for i in range(2,int(math.sqrt(n)+1)):
            if n%i==0:
                summ+=i
                if i!=n//i:
                    summ+=n//i
        return summ==n
            
        
print(solution())
