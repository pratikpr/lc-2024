# Given an array of integers, nums, and an integer value, target, determine if there are any three integers in nums whose sum is equal to the target, that is, nums[i] + nums[j] + nums[k] == target. Return TRUE if three such integers exist in the array. Otherwise, return FALSE.

def find_sum_of_three(nums, target):
    nums.sort()
    
    for i in range(len(nums)):
        req = target - nums[i]
        
        l, r = i+1, len(nums)-1
        while l < r:
            if nums[l] + nums[r] == req:
                return True
            elif  nums[l] + nums[r] > req:
                r -= 1
            else:
                l += 1
                
    return False

nums = [3,7,1,2,8,4,5]
target = 10
print(find_sum_of_three(nums, target))

nums = [-1,2,1,-4,5,-3]
target = -8
print(find_sum_of_three(nums, target))
