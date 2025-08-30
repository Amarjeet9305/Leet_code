# Write a program for to check as per given two tree same or not
# Condition is to check root node to child node left to right same element
# using Recursive approach

# First create a Tree node

class TreeNode(object):
    def __init__(self,val = 0, left=None, right= None):
        self.val = val
        self.left = left
        self.right = right
# Define a class
class Solution(object):
    def isSameTree(self,p,q):
        # If both are empty
        if not p and not q:
            return True
        # If one is none not other
        
        if not p or not q:
            return False
        # Check Recursively left and right subtree
        return (p.val, q.val and
                self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
# Driver code
# Case1
# p = TreeNode(1,TreeNode(2), TreeNode(3))
# q = TreeNode(1, TreeNode(2), TreeNode(3))

# Case 2
p = TreeNode(1, TreeNode(3))
q = TreeNode(3, TreeNode(1))    

sol = Solution()
print(sol.isSameTree(p,q))
        
    

            
        