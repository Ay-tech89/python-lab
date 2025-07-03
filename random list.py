import random

def fill_list(lst,limit_num,low,high):
    for i in range(limit_num):
        lst.append(random.randint(low,high))
        
minimum = int(input("Minimum number : "))
maximum = int(input("Maximum number : "))
n = int(input("Numbers limit : "))
a =[]
fill_list(a,n,minimum,maximum)
print("result is : ",a)
