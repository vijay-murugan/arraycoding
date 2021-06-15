
def non_rep(arr):
    rep_dic = dict()
    for i in range(len(arr)):
        if arr[i] in rep_dic:
            rep_dic[arr[i]] += 1
        else:
            rep_dic [arr[i]] = 1
    for i in range((len(arr))):
        if(rep_dic[arr[i]] == 1):
            return arr[i]

arr = [9, 4, 9, 6, 7, 4]
print(non_rep((arr)))