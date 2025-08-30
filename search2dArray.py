# Write a program will to find random element on 2-D array with given target element
# Approach will to used binary search 

# Creating a function defintion

def search2DArray(arr, target):
        
        # Calculate the array length
        
        m = len(arr)
        
        # Check Wheter condition is true
        
        if m == 0:
            return False
        n = len(arr[0])
        
        left, right = 0, m*n-1
        
        while left < = right:
            mid = left+(right - left) // 2
            mid_element = arr[mid // 2] [mid % 2]
            
            if target == mid_element:
                
                return True
            elif target < mid_element:
                right = mid - 1
            else:
                left = mid + 1
        return False
# Driver code

arr = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

target = 3

result = search2DArray(arr,target)

print(result)
                 