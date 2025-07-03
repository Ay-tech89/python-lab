orig = int(input("Enter a number: "))
num = orig
rev = 0
while num >0:
    digit = num%10
    rev = rev*10+digit
    num = int(num/10)
if orig == rev:
    print('It is a Palindrome')
else:
    print('It is Not a Palindrome')
