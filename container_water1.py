# Write a program container with most water given graph to finding max value contain water
# So we are applying approach on optimal solution like as [this is a two pointer problem
# will to finding left>right pointer then finding a max container water]
# And total time complexity is contain o(n) that means linear time

# Driver code

class Solution(object):
    # Define the class
    def maxArea(self,height):
        left , right = len(height) - 1
        max_water = 0
        
        while left < right:
            water = min(height[left],height[right]) * (right - left)
            max_water = max(max_water,water)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water

solution = Solution()

height = [1,8,6,2,5,4,8,3,7]
print(solution.maxArea(height))
                