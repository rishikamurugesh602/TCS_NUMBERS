n=int(input())
def sum_of_numbere(n):
    if n==1:
        return 1
    return n+sum_of_numbere(n-1)
print(sum_of_numbere(n))
