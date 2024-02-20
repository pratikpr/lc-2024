def moveZeroes(nums):
    i, j = 0, 0
    
    while i < len(nums):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
        i += 1
        
    while j < len(nums):
        nums[j] = 0
        j += 1
        

nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)