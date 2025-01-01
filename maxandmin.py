def maxmin(arr):
    maximum = arr[0]
    minimum = arr[0]
    for i in arr:
        if i > maximum:
            maximum = i
        elif i < minimum:
            minimum = i

    return minimum,maximum

arr = [1,2,3,4,5,6,-7]
ans = maxmin(arr)
print(ans)
    
