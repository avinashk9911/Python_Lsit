# In this question we will find, minimum jump required to reach at the end of the arry.

# we have assumend that we will reach at the end in every array
# For the arrays which also needs to check if we can reach at the end or not we have solved Jump_game_3.py

# Solution is inspired by :https://youtu.be/9kyHYVxL4fw?si=ClSVFACcLH0PoPXc

# In this question we will find, minimum jump required to reach at the end of the arry.

# we have assumend that we will reach at the end in every array
# For the arrays which also needs to check if we can reach at the end or not we have solved Jump_game_3.py

# Solution is inspired by :https://youtu.be/9kyHYVxL4fw?si=ClSVFACcLH0PoPXc

def jump(arr):
    n = len(arr)-1
    total_jump = 0
    coverage = 0
    lastjumpidx  = 0

    if n == 0:
        return 0

    for  i in range(0,len(arr)):

        coverage = max(coverage, i + arr[i])

        if i == lastjumpidx:
            lastjumpidx = coverage
            total_jump +=1

            if(coverage >= n):
                return total_jump
            
    return total_jump

arr = [2,4,1,2,3,1,1,2]
print(jump(arr))