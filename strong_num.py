n = int(input())

def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)

def solution():
    summ = 0
    temp = n

    while temp > 0:
        last_digit = temp % 10
        summ += factorial(last_digit)
        temp //= 10

    return summ == n

print(solution())
