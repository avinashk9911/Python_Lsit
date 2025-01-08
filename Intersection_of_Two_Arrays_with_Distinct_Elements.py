# Intersection of Two Arrays with Distinct Elements

# Given two arrays a[] and b[] with distinct elements of size n and m respectively, 
# the task is to find intersection (or common elements) of the two arrays. 
# We can return the answer in any order.

def intersect(a, b):
  
    # Put all elements of a[] in hash set
    st = set(a)
    res = []
    for i in range(len(b)):
      
        # If the element is in st
        # then add it to result array
        if b[i] in st:
            res.append(b[i])

    return res

a = [5, 6, 2, 1, 4]
b = [7, 9, 4, 2]

print(intersect(a,b))