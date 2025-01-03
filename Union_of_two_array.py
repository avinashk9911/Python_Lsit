# Union of Two Sorted Arrays

# Given two sorted arrays a[] and b[], 
# the task is to to return union of both the arrays in sorted order. 
# Union of two arrays is an array having all distinct elements that are present in either array. 
# The input arrays may contain duplicates.

def uniounarray(arr1,arr2):
    n = len(arr1)
    m = len(arr2)

    result = []

    i,j = 0,0

    while i<n and j<m:
        
        if i > 0  and arr1[i-1] == arr1[i]:
            i+=1
            continue

        if j > 0 and arr2[j-1] == arr2[j]:
            j+=1
            continue

        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i+=1
        elif arr1[i] > arr2[j]:
            result.append(arr2[j])
            j+=1
        else:
            result.append(arr2[j])
            i+=1
            j+=1

    while i < n:

        if i > 0  and arr1[i-1] == arr1[i]:
            i+=1
            continue
        result.append(arr1[i])
        i+=1

    while j < m:
        if j > 0 and arr2[j-1] == arr2[j]:
            j+=1
            continue
        result.append(arr2[j])
        j+=1

    return result


arr1 = [3, 5, 10, 10, 10, 15, 15, 20]
arr2 = [5, 10, 10, 15, 30]
print(uniounarray(arr1,arr2))



