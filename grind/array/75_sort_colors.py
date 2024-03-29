# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

def sortColors(nums):
    i, curr, j = 0, 0, len(nums)-1
    
    while curr <= j:
        if nums[curr] == 0:
            nums[i], nums[curr] = nums[curr], nums[i]
            i += 1; curr += 1
        elif nums[curr] == 2:
            nums[j], nums[curr] = nums[curr], nums[j]
            j -= 1
        else:
            curr += 1
            
nums = [2,0,2,1,1,0]
sortColors(nums)
print(nums)

nums = [2,0,1]
sortColors(nums)
print(nums)
