n,m=input().split()
n=int(n.split("=")[1])
m=int(m.split("=")[1])
def greatest(n,m):
    if n>m:
        return n
    else:
        return m
print(greatest(n,m))
