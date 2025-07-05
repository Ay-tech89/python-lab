def main():
    l = [36,78,90,34,12,34,13,74]
    n = len(l)
    print("Original list : ", l)
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j] , l[j+1] = l[j+1], l[j]
    print("List after sorting is : ", l)
main()