# Given an array arr[] of n elements that contains elements from 0 to n-1, with any of these numbers appearing any number of times. The task is to find the repeating numbers.

# Note: The repeating element should be printed only once.

# Example: 

# Input: n = 7, arr[] = [1, 2, 3, 6, 3, 6, 1]
# Output: 1, 3, 6
# Explanation: The numbers 1 , 3 and 6 appears more than once in the array.


# code from GFG

def findDuplicates(arr):
    n = len(arr)
    freqArr = [0] * n
    result = []

    for num in arr:
        freqArr[num] += 1

    for i in range(n):
        if freqArr[i] > 1:
            result.append(i)

    if not result:
        result.append(-1)

    return result


if __name__ == "__main__":
    arr = [1, 6, 5, 2, 3, 3, 2]
    duplicates = findDuplicates(arr)

    for element in duplicates:
        print(element, end=" ")