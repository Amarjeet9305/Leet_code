class Solution(object):
    def arrPairsum(self, nums):
        nums.sort()
        total = 0
        for i in range(0, len(nums),2):
            total += nums[i]
        return total
# Driver code to test the function
sol = Solution()
nums = [1,4,3,2]
print(sol.arrPairsum(nums))        
    