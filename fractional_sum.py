num1=int(input())
den1=int(input())
num2=int(input())
den2=int(input())
def gcd(a,b):
    while a>0 and b>0:
        if a>b:
            a=a%b
        else:
            b=b%a
    if a==0:
        return b
    return a
def lcm(a,b):
    return (a*b)/gcd(a,b)
def solution():
    
    temp=int(lcm(den1,den2))
    num=(num1*temp//den1)+(num2*temp//den2)
    den=temp
    return f"{num}/{den}"
    
print(solution())
