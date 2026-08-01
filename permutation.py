n,r=map(int,input().split())
def solution():
    ans=1
    for i in range(n,n-r,-1):
        ans*=i
    return ans
print(solution())
