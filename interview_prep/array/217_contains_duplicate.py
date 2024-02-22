# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def containsDuplicate(nums) -> bool:
    return len(set(nums)) != len(nums)

def containsDuplicateSort(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
        
    return False

nums = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicateSort(nums))

nums = [1,2,3,1]
print(containsDuplicateSort(nums))

nums = [1,2,3,4]
print(containsDuplicateSort(nums))