def sum0(arr):
    s = set()
    sum_ = 0
    for i in range(len(arr)):
        sum_ += arr[i]
        if sum_ == 0 or sum_ in s:
            return True
        s.add(sum_)
    return False
arr = [6,3,-1,-2,4]
print(sum0(arr))