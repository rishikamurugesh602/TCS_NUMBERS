n=int(input())
def isPrime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
        

def solution():
    for i in range(1,n//2+1):
        if isPrime(i) and isPrime(n-i):
            return ((i,n-i))
    return False
print(solution())
