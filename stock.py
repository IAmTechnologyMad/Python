def findTriplets(arr, n):
    flag = 0

    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):

                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])
                    flag = 1
    
    if (flag == 0):
        print("not found")


arr = [0, -1, 2, -3, 1]
n = len(arr)
findTriplets(arr, n)
















