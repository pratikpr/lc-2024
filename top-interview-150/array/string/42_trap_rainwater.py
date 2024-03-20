# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

def trap(height) -> int:
    l, r = 0, len(height)-1
    left_max, right_max = 0, 0
    result = 0
    
    while l < r:
        if height[l] < height[r]:
            if height[l] >= left_max:
                left_max = height[l]
            else:
                result += left_max-height[l]
            l += 1
        else:
            if height[r] >= right_max:
                right_max = height[r]
            else:
                result += right_max-height[r]
            r -= 1  
    return result 

height = [4,2,0,3,2,5]
print(trap(height))

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))