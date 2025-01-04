# Given two arrays a[] and b[], the task is to return union of both the arrays in any order.

# Note: Union of two arrays is an array having all distinct elements that are present in either array.

# Input : a[] = {1, 2, 3, 2, 1}, b[] = {3, 2, 2, 3, 3, 2}
# Output : {3, 2, 1}
# Explanation: 3, 2 and 1 are the distinct elements present in either array.

# Input : a[] = {1, 2, 3}, b[] = {4, 5, 6}
# Output : {1, 2, 3, 4, 5, 6}
# Explanation: 1, 2, 3, 4, 5 and 6 are the elements present in either array.


# Method 1: We will be using Set() data structure as it doesn't contain dublicate values.


#************In python we have set() data type, that's why it was easy for us but in Java Hash Set is
#            very deficult to implement**************************************************************

def findUnion(arr1, arr2):

    items = set()

    for i in arr1:
        items.add(i)

    for i in arr2:
        items.add(i)

    result = []

    for i in items:
        result.append(i)

    return result

arr1  = [1, 2, 3, 2, 1]
arr2 = [3, 2, 2, 3, 3, 2]
print(findUnion(arr1, arr2))