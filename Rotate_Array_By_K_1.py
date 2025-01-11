# This is the question that I made for my own practice after solving "rotate array by one".
# The main motive of this question was, what if we need to cyclically roate an array by any given integer K

# we have been given a array a[]  and an integer K. We need to cyclically right-rotate the array by K

def method1(arr,k): 

    def rotate(start,end):
        while start <= end:
            arr[start],arr[end] = arr[end],arr[start]
            start +=1
            end -=1

    # rotate the whole
    rotate(0,len(arr)-1)

    # rotate the first K element
    rotate(0,k-1)

    # rotate remaining array
    rotate(k,len(arr)-1)

    return arr

arr = [1, 2, 3, 4, 5]
k = 5
print(method1(arr,k))

arr1 = [-1, -2, -3, -4, -5]
k1 = 2
print(method1(arr1,k1))


    

        