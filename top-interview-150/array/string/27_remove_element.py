# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.

def removeElement(nums, val: int) -> int:
    i, j = 0, 0
    
    while i < len(nums):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
        i += 1
            
    return j


def removeElement2(nums, val):
    i, j = 0, len(nums)-1

    while i <= j:
        while i <= j and nums[j] == val:
            j -= 1
        if nums[i] == val:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    return i


nums = [0,1,2,2,3,0,4,2]; val = 2
print(removeElement2(nums, val))

nums = [3,2,2,3]; val = 3
print(removeElement2(nums, val))