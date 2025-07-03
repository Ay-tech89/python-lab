def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
// for not receving the decimal number
% for Remainder
Enter the operation: ''')

    num1 = int(input('Please enter the first number: '))
    num2 = int(input('Please enter the second number: '))
    if operation == '+':
        print("The result is : ",num1 + num2)
    elif operation == '-':
        print("The result is : ",num1 - num2)
    elif operation == '*':
        print("The result is : ",num1 * num2)
    elif operation == '/':
        print("The result is : ",num1 / num2)
    elif operation == '//':
        print("The result is : ",num1 // num2)
    elif operation == '%':
        print("The result is : ",num1 % num2)
    else:
        print('You have not typed a valid operator, please run the program again.')
calculate()