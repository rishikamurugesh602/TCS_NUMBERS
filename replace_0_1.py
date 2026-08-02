n=input()

def solution():
    num=int(n)
    numm=""
    while num>0:
        last_digit=num%10
        if last_digit==0:
            last_digit=1
        numm+=str(last_digit)
        num//=10
    return numm[::-1]
print(solution())
