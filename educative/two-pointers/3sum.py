# Given an array of integers, nums, and an integer value, target, determine if there are any three integers in nums whose sum is equal to the target, that is, nums[i] + nums[j] + nums[k] == target. Return TRUE if three such integers exist in the array. Otherwise, return FALSE.

def find_sum_of_three(nums, target):
    nums.sort()
    
    for num in range(len(nums)):
        l, r = num+1, len(nums)-1
        
        while l < r:
            _sum = nums[num] + nums[l] + nums[r]
            if _sum == target:
                return True
            elif _sum > target:
                r -= 1
            else:
                l += 1
                
    return False

nums = [1,-1,0]; target = -1
print(find_sum_of_three(nums, target))

nums = [-1,2,1,-4,5,-3]; target = -8
print(find_sum_of_three(nums, target))

nums = [-1,2,1,-4,5,-3]; target = -8
print(find_sum_of_three(nums, target))
