# Write a program container with most water given array element hieght
# height=[1,8,6,2,5,4,8,3,7] finding two lines that together with the x-axis from a container
# such that container contain the most water,and expected ouput 49 
# Constraint given amount of water min(height[i],height[j],*(j-i))

# There are two approach first is Brute force and two pointer like optimal solution.
# Brute force that can check all pairs(i,j) compute the water and return maximum


# define function

def maxArea(height):
    
    # Store all maximum value of containing water
    max_water = 0
    
    l = len(height)
    for i in range(l):
        # outer loop
        for j in range(i+1,l):
            # inner loop compute n times
            water = min(height[i],height[j]) * (j-i)
            max_water = max(max_water,water)  
    return max_water

# Driver code

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))             
