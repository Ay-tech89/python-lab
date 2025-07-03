n = int(input("Enter the number of subjects: "))
l = list()
for i in range(n):
    x = float(input("Enter the marks: "))
    l.append(x)
print(l, "is the given list of marks.")
print()
total = int(input("Enter the total marks of subject : "))
ntotal = n*total
f = sum(l)
print("Total marks: ", f)
print("Percentage: ", (f/ntotal)*100)
