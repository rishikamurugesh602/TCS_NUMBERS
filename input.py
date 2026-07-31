n,m=input().split()
n=int(n.strip('""'))
m=int(m.strip('""'))
def greatest(n,m):
    if n>m:
        return n
    else:
        return m
print(greatest(n,m))
