# You are given an array arr and an integer k. Write a code to rotating the elements based on k:
# arr = [-1, -2, -3, -4, -5]
# k = 2
# Output = [-5, -2, -4, -3, -1]
# arr = [1, 2, 3, 4, 5, 6]
# k = 3
# Output =[6, 5, 4, 2, 3, 1]
# arr = [10, 20, 30, 40]
# k = 1
# output =  [40, 10, 20, 30 ]

def method1(arr,k):
    i = 0
    j = len(arr)-1
    k = (len(arr)-1)-k  # we are placing the pointer K just before the k

    while i < k and k < j:

        arr[i],arr[j],arr[k] = arr[j],arr[k],arr[i]

        i+=1
        k-=1
        j-=1
        # print(arr)

    if i == k:
        arr[i],arr[j] = arr[j],arr[i]
        # print(f'final swap {arr}')

    return arr

arr = [-1, -2, -3, -4, -5]
k = 2
print(method1(arr,k))

arr1 = [-5, -2, -4, -3, -1]
k1 = 2
print(method1(arr1, k1))

arr2 = [10, 20, 30, 40]
k2 = 1
print(method1(arr2, k2))