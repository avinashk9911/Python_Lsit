#given a array of non negative integer, you are inetially positioned at the 1st index of the array
# Each element in the array represent you maximum jump length at the position.
# determine if you are able to reach at the last index of that array.


# this solution I found on youtube neetcode: https://youtu.be/Yan0cv2cLy8?si=RpUAWVEUgC_mSxOo

def jump(arr):
    goal = len(arr)-1
    for i in range(len(arr)-1,-1,-1):
        if i+arr[i] >= goal:
            goal = i
    
    return True if goal == 0 else False

arr = [1,3,5,8,9,2,6,7,6,8,9]
print(jump(arr))

arr1 = [3,2,1,0,4]
print(jump(arr1))