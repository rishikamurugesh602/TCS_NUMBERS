n = int(input())

def solution():
    ans = str(n * n)
    return ans.endswith(str(n))

print(solution())
