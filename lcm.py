n1, n2 = input().split()

a = int(n1)
b = int(n2)

def lcm(a, b):
    maximum = max(a, b)

    while True:
        if maximum % a == 0 and maximum % b == 0:
            return maximum
        maximum += 1

print(lcm(a, b))
