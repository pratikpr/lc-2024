# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

def trap(height) -> int:
    left_max, right_max = [], []
    
    left_max.append(height[0])
    for i in range(1, len(height)):
        left_max.append(max(height[i], left_max[i-1]))
        
    right_max.append(height[-1])
    for i in range(len(height)-2, -1, -1):
        right_max.insert(0, max(height[i], right_max[0]))
    
    # print(left_max, right_max)
    res = 0
    for i in range(1, len(height)-1):
        res += min(left_max[i], right_max[i]) - height[i]
        
    return res

height = [4,2,0,3,2,5]
print(trap(height))

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))