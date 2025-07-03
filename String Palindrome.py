str1 = input("Enter the string : ")
length = len(str1)
x = length-1
index =0
while(index<x):
    if(str1[index])==str1[x]:
        index=index+1
        x = x-1
    else:
        print("String is not a palindrome")
        break
else:
    print("String is a plaindrome")