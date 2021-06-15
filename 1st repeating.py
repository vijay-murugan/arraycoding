arr = [6, 10, 5, 4, 9, 120, 4, 6, 10]
new_list = list()
rep_list = list()
mini = len(arr)
for i in range(len(arr)):
    if arr[i] in new_list:
        rep_list.append(arr[i])
    else:
        new_list.append(arr[i])
for i in range(len(rep_list)):
    for j in range(len(arr)):
        if arr[j] == rep_list[i] and mini > j :
            mini = j

print(arr[mini])
