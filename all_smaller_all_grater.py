#Element with left side smaller and right side greater
#Given an unsorted array of arr. 
# Find the first element in an array such that all of its left elements are smaller 
# and all right elements of its are greater than it.
#Note: Return -1 if there is no such element.

# method 1: this is my solution which is not that effecient in time complexity. 
# But the second 'while' condition  and 'if' condition gave me good understanding of how 
# we should use range of 'r' and l == -1 and r == len(arr). This is a good understanding because I didn't gussed it earlier

def method1(arr):
    ans = -1
    i = 1

    while i < len(arr):

        l = i-1
        r = i+1

        while l>=0 and (arr[l] < arr[i]):
            l-=1
        while r < len(arr) and (arr[r]> arr[i]):
            r+=1

        if l == -1 and r == len(arr):
            ans = arr[i]
            break
        i+=1

    return ans

arr = [4,2,5,7]

answer = method1(arr)
print(answer)

# method 2:  This is the concept that I also have not understood well, as how someone can comeup with this solution
# but after looking to a you tube video I understand the code. (https://youtu.be/_QsA70cqzG0?si=rq3Eo74mD2vm-hOB)
# To Understand the code I still need to understand how we are reaching to this solution 

def method2(arr):

    ans = -1

    if len(arr) < 3:
        return ans
    
    leftmax = [arr[0]]*(len(arr))
    maxleft = arr[0]

    rightmin = [arr[len(arr)-1]]*(len(arr))
    minright = arr[len(arr)-1]

    for i in range(0, len(arr)):

        if arr[i] > maxleft:
            maxleft = arr[i]

        leftmax[i]  = maxleft
    
    print(leftmax)

    for i in range(len(arr)-1, -1, -1):

        if arr[i] < minright:
            minright = arr[i]

        rightmin[i] = minright

    print(rightmin)

    for i in range(0,len(arr)):

        if i != 0 and i != len(arr)-1:   # this codition is to avoide 1st and last number as they have no left and right respectively numbers to them.
            if leftmax[i] == rightmin[i]:
                ans = leftmax[i]
                break
    
    return ans

arr1 = [4,3,2,7,8,9]
answer1 = method2(arr1)
print(answer1)

        
        



