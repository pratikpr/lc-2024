# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]
    
    return None


def twoSumHash(nums, target):
    indexes = {}
    
    for i, n in enumerate(nums):
        indexes[n] = i

    for i, n in enumerate(nums):
        if target-n in indexes and i != indexes[target-n]:
            return [i, indexes[target-n]]
        
    return None
        
nums = [2,7,11,15]; target = 9
print(twoSumHash(nums, target))

nums = [3,2,4]; target = 6
print(twoSumHash(nums, target))

nums = [3,3]; target = 6
print(twoSumHash(nums, target))