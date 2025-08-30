# Write a program to find the center of graph as per given edges.

class Solution:
    def lookCenter(self,edges):
        # First take two edges
        a,b = edges[0]
        c,d = edges[1]
    # If the common node is center
        if a == c or a == d:
            return a
        else:
            return b
# Driver code
# Test Case1
sol = Solution()
edges = [[1,2],[2,3],[4,2]] 
print(sol.lookCenter(edges))   

# Test case2
edges = [[1,2],[5,1],[1,3],[1,4]]
print(sol.lookCenter(edges))        
        
    
