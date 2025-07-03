emails = tuple()
username = tuple()
domainname = tuple()
n = int(input("How many email ids you want to enter?: "))
for i in range(0,n):
    emid = input("> ")
    emails = emails +(emid,)
    spl = emid.split("@")
    username = username + (spl[0],)
    domainname = domainname + (spl[1],)

print("\nThe email ids in the tuple are :")
print(emails)
print("The username in the email ids are :",username)
print("\nThe domain name in the email ids are :")
print(domainname)


