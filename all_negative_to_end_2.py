# The task is to place all negative elements at the end of the array 
# without changing the order of positive elements and negative elements.
#https://youtu.be/Jc6vv-m8oWw?si=_MYegshA0Cu7pOwx
def method1(arr):
    temp = [1]* (len(arr))
    j = 0
    for i in range(len(arr)):
        if arr[i] >= 0:
            temp[j] =  arr[i]
            j+=1
    for i in range(len(arr)):
        if arr[i] < 0:
            temp[j] =  arr[i]
            j+=1

    for i in range(len(arr)):
        j = i
        arr[i]= temp[j]

    print(arr)

arr = [-5, 7, -3, -4, 9, 10, -1, 11]

method1(arr)

        

