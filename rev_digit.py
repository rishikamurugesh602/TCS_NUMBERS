s=input()
n=int(s)
def solution(n):
    rev_dig=0
    while n>0:
        last_dig=n%10
        rev_dig=rev_dig*10+last_dig
        n//=10
    return rev_dig
print(solution(n))
    
