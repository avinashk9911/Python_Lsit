# Given two sorted arrays a[] and b[] with distinct elements of size n and m respectively, 
# the task is to find intersection (or common elements) of the two arrays. 
# We need to return the intersection in sorted order.

# Note: Intersection of two arrays can be defined as a set containing 
# distinct common elements between the two arrays.

# Examples:

# Input: a[] = { 1, 2, 4, 5, 6 }, b[] = {  2, 4, 7, 9 }
# Output: { 2, 4 }
# Explanation: The common elements in both arrays are 2 and 4.

# Input: a[] = { 2, 3, 4, 5 }, b[] = { 1, 7 }
# Output: { }
# Explanation: There are no common elements in array a[] and b[].

def method1(arr1,arr2):

    set1 = set(arr1)
    set2 = set(arr2)

    res = []

    for i in set1:
        if i in set2:
            res.append(i)

    return res

arr11 = [1, 2, 4, 5, 6]
arr22= [2, 4, 7, 9 ]

print(method1(arr11,arr22))

# code form leetcode. link: https://youtu.be/fwUTXaMom6U?si=vYog3q3tl5ZYV4GI

def method2(arr1,arr2):

    set1 = set(arr1)

    result = []

    for i in arr2:
        if i in set1:
            result.append(i)
            set1.remove(i)
    
    return result

arr1 = [2, 3, 4, 5 ]
arr2 = [1, 7 ]
print(method2(arr1,arr2))
        