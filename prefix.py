def prefix(name,gender):
    if (gender == 'M' or gender == 'm'):
        print("Hello, Mr.",name)
    elif (gender == 'F' or gender == 'f'):
        print("Hello, Ms.",name)
    else:
        print("Please enter only M or F in gender")
name = input("Enter your name: ")
gender = input("Enter your gender: M for Male, and F for Female: ")
prefix(name,gender)
