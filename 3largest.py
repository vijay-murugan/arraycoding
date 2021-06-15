def largest3(arr):
    first = second = third = -1
    first = max(arr)
    arr.remove(first)
    second = max(arr)
    arr.remove(second)
    third = max(arr)
    print(first, second, third)


arr = [10, 4, 3, 50, 23, 90]
largest3(arr)