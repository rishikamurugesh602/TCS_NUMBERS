n = int(input())

def armstrong(n):
    k = len(str(n))
    temp = n
    summ = 0

    while n > 0:
        tp = n % 10
        summ += tp ** k
        n //= 10

    return summ == temp

if armstrong(n):
    print("yes")
else:
    print("no")
