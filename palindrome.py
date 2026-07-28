n=int(input())
def palindrome(n):
    rev=0
    dup=n
    while n>0:
        ld=n%10
        rev=(rev*10)+ld
        n//=10
    return dup==rev
number = 4554  
if palindrome(number):  
  
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
