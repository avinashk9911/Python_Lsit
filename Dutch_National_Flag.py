def dutchnational(arr):
    i = 0
    j = 0
    k = len(arr)-1
    while j<=k:
        if arr[j] == 0:
            arr[j], arr[i] = arr[i], arr[j]
            i+=1
            j+=1
        elif arr[j]==2:
            arr[j], arr[k] = arr[k], arr[j]
            k-=1
        elif arr[j] == 1:
            j+=1
    print(arr)

arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
dutchnational(arr)