n=int(input())
def prime_factors(n):
    res=[]
    for i in range(2,n+1):
        
        if n%i==0:
            prime=True
            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                    prime=False
                    break
            if prime:
               res.append(i)
    return res
print(prime_factors(n))
