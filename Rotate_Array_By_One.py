# Rotate Array By One : given an array, the task is to cyclically right-rotate the array by one. 

# Method1: This is written by me, but the drawback of this function is that, it will only rotate the array 
# by one only i.e. if we ask the array to rotate by 2 or 3, it will not work

def rotate1(arr):
    previous = arr[0]
    i = 1
    while i<len(arr):
        previous, arr[i] = arr[i], previous
        i+=1
    arr[0],previous = previous,arr[0]
    return arr

print(rotate1([1,2,3,4,5]))
print(rotate1([2,3,4,5,1]))


# Mehtod2: Using Two Pointers

# We can use two pointers, As we know in cyclic rotation 
# we will bring last element to first and shift rest in forward direction, 
# we can do this by swapping every element with last element till we get to the last point.

def rotate2(arr):
    i = 0 
    j = len(arr)-1

    while i < j:
        arr[i],arr[j] = arr[j],arr[i]
        i+=1
    return arr

print(rotate2([1,2,3,4,5,6]))
print(rotate2([2,3,4,5,6,1]))


