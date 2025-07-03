t1 = tuple()
n = int(input("Total no. of values in first tuple : "))
for i in range(n):
    a = input("Enter element : ")
    t1 = t1+(a,)
    t2 = tuple()
m = int(input("Total no. of values in Second tuple : "))
for i in range(m):
    a = input("Enter element : ")
    t2 = t2+(a,)
print("First tuple : ",t1)
print("Second tuple : ",t2)
t1,t2=t2,t1
print("First tuple : ",t1)
print("Second tuple : ",t2)
