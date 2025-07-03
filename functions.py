def calculate():
        print("\n1.  Area of Circle\t\t" "2.  Area of Square")
        print("3.  Area of Rectangle\t" "4.  Circumference of Circle")
        print("5.  Perimeter of Rectangle\t" "6.  Perimeter of Square")
        print("7.  Perimeter of Triangle\t" "8.  mathematical operations")

        num=int(input("\nEnter your choice: "))

        if num==1:
            radius=int(input("Enter the radius of Circle: "))
            a=3.14*radius*radius
            print("Area of Circle: ",a)
        elif num==2:
            length=int(input("Enter the side of the square: "))
            a=length*length
            print("Area of Square: ",a)
        elif num==3:
            length=int(input("Enter the length of the Rectangle: "))
            Breadth=int(input("Enter the breadth of the Rectangle: "))
            a=length*Breadth
            print("Area of Rectangle: ",a)
        elif num==4:
            radius=int(input("Enter the radius of Circle: "))
            a=2*(int(3.14*radius))
            print("Circumference of Circle: ",a)
        elif num==5:
            length=int(input("Enter the length of the Rectangle: "))
            Breadth=int(input("Enter the breadth of the Rectangle: "))
            a=2*(int(length+Breadth))
            print("Perimeter of Rectangle: ",a)
        elif num==6:
            length=int(input("Enter the side of the square: "))
            a=4*length
            print("Perimeter of Square: ",a)
        elif num==7:
            a=int(input("Enter the side of the square: "))
            b=int(input("Enter the side of the square: "))
            c=int(input("Enter the side of the square: "))
            x=a+b+c
            print("Perimeter of Triangle :",x)
        elif num==8:
            operation = input('''
Please type the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
// for Integer Division
Enter the operation: '''
)
            number_1 = int(input('Please enter the first number: '))
            number_2 = int(input('Please enter the second number: '))

            if operation == '+':
               print("Sum of numbers: ",number_1 + number_2)

            elif operation == '-':
               print("Subtraction of numbers: ",number_1 - number_2)
  
            elif operation == '*':
               print("Multiplication of numbers: ",number_1 * number_2)

            elif operation == '/':
               print("Division of numbers:",number_1 / number_2)
   
            elif operation == '//':
               print("Integer division of numbers: ",number_1 // number_2)
            else:
               print('You have not typed a valid operator, please run the program again.')    
        else:
            print("Invalid option")

        again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print( '''
See you later.
Keep Smiling
And Stay Happy
''')
    else:
        again()
        
calculate()

            
        
        
        
