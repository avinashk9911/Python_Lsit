# K’th Smallest/Largest Element in Unsorted Array | Expected Linear Time

# 1) brute force approch - just sort the array and print the k'th element

# 2) by this functon we will get three smallest element sub array and this is not the correct solution

def ksmall(arr):
    temp = [arr[0],arr[0],arr[0]]
    for i in arr:
        if i < temp[2]:
            temp[0]=temp[1]
            temp[1]=temp[2]
            temp[2]=i
        elif i< temp[1]:
            temp[0]=temp[1]
            temp[1]=i
        # elif i< temp[0]:
        #     temp[0]= i

    return temp

# arr = [1,2,3,4,5,6,7,0,-1,-2,-3]
arr1 = [-2,-3]
# answer = ksmall(arr1)
# print(answer)


# 3) this is not working but the concept that I thought was correct. May be there is some problem
#     with function call and arr inetialization.

# import random

# def arrange(arr,pevit):
#     # pevit = random.randint(0, len(arr)-1)
#     # pevit = len(arr)-1
#     # print(pevit)
#     point =  0
#     i=0
#     while i<len(arr)-1:
#     # while i<pevit:
#         if arr[i]<=arr[pevit]:
#             arr[i], arr[point] = arr[point],arr[i]
#             i+=1
#             point+=1
#         else:
#             i+=1
#     arr[point],arr[pevit] = arr[pevit],arr[point]

#     # print(arr)
#     # print(point)
#     return point

# def kthsmall(arr,k):
#     positon = (len(arr)-1)-k
#     pevit = len(arr)-1
#     point = arrange(arr,pevit)
#     if(point == positon):
#         return arr[positon]
#     if len(arr)>1:
#         if point > positon:
#             arrange(arr[:point+1],len(arr[:point])-1)
#         else:
#             arrange(arr[point:],len(arr[:point])-1)

# arr=[3,2,1,5,6,4]
# #arrange(arr)
# answer = kthsmall(arr,3)
# print(answer)




# this is the code that I have written from the help of you tube video
# link to that video: https://youtu.be/XEmy13g1Qxc?si=o2JjtmuC1K0jQ0ig

from typing import List 

class Solution:
    def Kthsmallest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickselect(l,r):
            pivot = nums[r]
            point = l
            
            for i in range(l,r):
                if nums[i]<= pivot:
                    nums[i],nums[point] = nums[point], nums[i]
                    point +=1

            pivot, nums[point] = nums[point], pivot

            if point < k:   return quickselect(l,point-1)
            elif point > k: return quickselect(point+1,r) 
            else:           return nums[point]
        
        return quickselect(0, len(nums)-1)

nums = [3, 2, 1, 5, 6, 4]
k = 3
Solution = Solution()
result = Solution.Kthsmallest(nums,k)
print(result)