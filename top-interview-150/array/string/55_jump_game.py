# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.
from typing import List

def canJump(nums: List[int]) -> bool:
    ways = [0] * len(nums)
    ways[0] = 1
    
    for i in range(len(nums)-1):
        j = 1
        while (i+j) < len(ways) and j <= nums[i]:
            ways[i+j] += 1
            j += 1    
                   
    for n in ways:
        if n == 0:
            return False
        
    return True


nums = [2,3,1,1,4]
print(canJump(nums))