s=input()
n=int(s)
def solution(n):
    rev_dig=0
    min_dig=float('inf')
    max_dig=float('-inf')
    while n>0:
        last_dig=n%10
        min_dig=min(min_dig,last_dig)
        max_dig=max(max_dig,last_dig)
        n//=10
    return min_dig,max_dig
print(solution(n))
    
