list1 = eval(input("Enter the list : "))
length = len(list1)
element = int(input("Enter the element to be searched : "))
for i in range(0,length):
    if element == list1[i]:
        print(element,"found at",i,"position")
        break
else:
    print(element,"not present in the list")
