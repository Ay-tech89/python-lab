dic = {}
while True:
    print("1. Add New Contact")
    print("2. Modify Phone Number of Contact")
    print("3. Delete a Friend's contact")
    print("4. Display all entries")
    print("5. Check if a friend is present or not")
    print("6. Display in sorted order of names")
    print("7. Exit")
    inp = int(input("Enter your choice(1-7): "))

    #Adding a contact
    if(inp == 1):
        contact = int(input("How many contacts you want to add : "))
        for i in range(contact):
            name = input("Enter your friend name: ")
            phonenumber = input("Enter your friend's contact number: ")
            dic[name] = phonenumber
            print("Contact Added \n")
        
    #Modifying a contact if the entered name is present in the dictionary
    elif(inp == 2):
        name = input("Enter the name of friend whose number is to be modified: ")
        if(name in dic):
            phonenumber = input("Enter the new contact number: ")        
            dic[name] = phonenumber
            print("Contact Modified\n\n")
        else:
            print("This friend's name is not present in the contact list")
            
    #Deleting a contact if the entered name is present in the dictionary
    elif(inp == 3):
        name = input("Enter the name of friend whose contact is to be deleted: ")
        if(name in dic):
            del dic[name]
            print("Contact Deleted\n\n")
        else:
            print("This friend's name is not present in the contact list")
            
    #Displaying all entries in the dictionary
    elif(inp == 4):
        print("All entries in the contact")
        for a in dic:
            print(a,"\t\t",dic[a])
        print("\n\n")
        
    #Searching a friend name in the dictionary
    elif(inp == 5):
        name = input("Enter the name of friend to search: ")
        if(name in dic):
            print("The friend",name,"is present in the list\n\n")
        else:
            print("The friend",name,"is not present in the list\n\n")
            
    #Displaying the dictionary in the sorted order of the names
    elif(inp == 6):
        print("Name\t\t\tContact Number")
        for i in sorted(dic.keys()):
            print(i,"\t\t\t",dic[i])
        print("\n\n")
        
    #Exit 
    elif(inp == 7):
        break
    else:
        print("Invalid Choice. Please try again\n")
