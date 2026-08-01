n = input()

def abundant(n):
    n1 = int(n)
    summ = 0

    for i in range(1, int(n1**0.5) + 1):
        if n1 % i == 0:
            summ += i

            if i != 1 and i != n1 // i:
                summ += n1 // i

    return summ > n1

print(abundant(n))
