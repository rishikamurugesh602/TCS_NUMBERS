a,r,n=map(int,input().split())
def gcd(a,r,n):
    return int((a*(r**n-1)/(r-1)))
print(gcd(a,r,n))
