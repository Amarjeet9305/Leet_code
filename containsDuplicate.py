# Given an integer array nums, return true if any value appears at least twice in the 
# array, and return false if every element is distinct.

# Creating a class

class Solution(object):
    def containsDuplicate(self,nums):
        
        seen = set()
        
        for num in nums:
            
            
            if num in seen:
                
                return True 
            seen.add(num)
        return False 
# Test case

sol = Solution()

print(sol.containsDuplicate([1,2,3,1]))

print(sol.containsDuplicate([1,2,3,4]))

print(sol.containsDuplicate([1,2,1,2,1,1]))    
       