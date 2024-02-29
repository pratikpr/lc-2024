# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

def threeSumClosest(nums, target) -> int:
    nums.sort()
    diff = float("inf")
    
    for i in range(len(nums)):
        l, r = i+1, len(nums)-1
        
        while l < r:
            _sum = nums[i] + nums[l] + nums[r]
            if abs(target - _sum) < abs(diff):
                diff = target - _sum
            if _sum > target:
                r -= 1
            else:
                l += 1
        if diff == 0:
            break
        
    return target - diff


nums = [-1,2,1,-4]; target = 1
print(threeSumClosest(nums))
