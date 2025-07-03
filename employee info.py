d1 = dict()
i = 1
n = int(input("Enter number of entries : "))
while i<=n:
    ID = int(input("\nEnter ID of the employee : "))
    Nm = input("Enter name of the employee : ")
    phone = int(input("Enter phone number : "))
    basic = int(input("Enter basic salary : "))
    d1[ID]=[Nm,phone,basic]
    i= i+1
l = d1.keys()
for i in l:
    print("\nID - ",i," : ")
    z = d1[i]
    print("Name\t\t","Phone number\t\t","salary")
    for j in z:
        print(j, end="\t\t")

    
    
