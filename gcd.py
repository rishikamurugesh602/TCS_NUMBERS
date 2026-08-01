# Read input
n1, n2 = input().split()

# Convert to integers
a = int(n1)
b = int(n2)

# Function to find GCD
def gcd(a, b):
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    if a == 0:
        return b
    else:
        return a

# Print answer
print(gcd(a, b))
