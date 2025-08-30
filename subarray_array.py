# Write a program find the total sub-array given array
# It is simple mathematical approach like finding sub-array Total sub-array = n.(n+1)/2
# Total time complexity o(n).

# Driver code

def count_total_subarray(arr):
    
    n = len(arr)
    
    total = n * (n + 1)//2
    
    return total

# Test case

arr = [1,2,3,4]
print(count_total_subarray(arr))
 