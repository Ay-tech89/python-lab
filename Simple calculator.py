result = 0 
value1 = float(input("Enter the value 1 : "))
value2 = float(input("Enter the value 2 : "))
ch = input("Enter any of the operator (+,-,*,/) : ")
if ch == "+":
    result = value1 + value2
elif ch == '-':
    if value1> value2:
        result = value1 - value2
    else:
        result = value2 -value1
elif ch == "*":
    result = value1 * value2
elif ch == "/":
    if value2 ==0:
        print("Please enter a value other than 0 ")
    else:
        result = value1/value2
else:
    print("Please enter any one of the operator (+,-,*,/) ")
print("The result is : ",result)