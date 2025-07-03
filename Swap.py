num=[3, 25, 13, 6, 35, 8, 14, 45]
for i in range(len(num) -1):
    if num[i+1] % 5 == 0 :
        num[i],num[i+1]=num[i+1],num[i]
print("result is : \n",num)
