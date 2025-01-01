# Move all negative numbers to beginning and positive to end with constant extra space

# imp : Order of elements is not important here (it dose not matter which +ve number is comming
#         after whome or which -ve number comes after which -ve number)


def negative(arr):
    i,j = 0,0
    while j<=len(arr)-1:
        if arr[j]<0:
            arr[i],arr[j] = arr[j], arr[i]
            i+=1
            j+=1
        else:
            j+=1
    
    print(arr)

arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
negative(arr)