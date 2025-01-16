def kedane(arr):
    startidx = 0
    endidx = 0
    final_max = arr[0]
    current_max = arr[0]
    i = 1
    while i < len(arr):
        temp_max =  current_max + arr[i]

        if i >= temp_max:
            startidx = i
            endidx = i
            current_max = arr[i]
            i+=1

        elif i < temp_max:
            endidx = i
            current_max = temp_max
            i+=1
        
        final_max = max(current_max,final_max)

    return (arr[startidx:endidx+1],final_max)


print(kedane([2,3,-8,7,-1,2,3]))