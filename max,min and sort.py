numbers = tuple()
n = int(input("How many numbers you want to enter? : "))
for i in range(0,n):
    num = int(input("Enter a number for tuple : "))
    numbers = numbers + (num,)
print("\nThe numbers in the tuple are : ",numbers)
print("\nThe maximum number is : ",max(numbers))
print("The minimum number is : ",min(numbers))
print("The sorted tuple is : ",sorted(numbers))
