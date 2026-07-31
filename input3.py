s=input()
n=s.strip('""')
listt=list(map(int,n.split()))

stringg=",".join(map(str,listt))
print(stringg)
