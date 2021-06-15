def largest3(arr):
    arr = sorted(arr)
    for i in range(len(arr)-1,len(arr)-4,-1):
        print(arr[i])


arr = [12, 45, 1, -1, 45, 54, 23, 5, 0, -10]
largest3(arr)