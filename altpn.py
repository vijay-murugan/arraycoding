arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
arr = sorted(arr)  # -4, -1, 1, 2, 3, 4
print(arr)
j = len(arr) - 1
for i in range(1, len(arr)):
    z = arr[i]  # -1
    if arr[j] > 0 and arr[i] < 0:  # 4 > 0 -1 < 0
        arr[i] = arr[j]  # -4 4 1 2 3 -1
        arr[j] = z
        if arr[j] > 0:
            j -= 1  #
    elif arr[j] < 0 and arr[i] > 0:
        arr[i] = arr[j]
        arr[j] = z

    print(arr)
