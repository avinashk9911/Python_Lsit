def mindiff(arr,k):
    
    arr.sort()
    n =  len(arr)

    current_diff = arr[-1]-arr[0]

    smallest = arr[0]+k
    largest = arr[0]-k

    for i in range(n-1):

        min_height = min(smallest, arr[i+1]-k)
        max_height = max(largest, arr[i]+k)

        current_diff = min(current_diff, max_height-min_height)

    return current_diff


arr = [12, 6, 4, 15, 17, 10]
k = 6
print(mindiff(arr,k))
    