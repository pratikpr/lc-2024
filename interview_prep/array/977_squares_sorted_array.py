# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

def sortedSquares(nums):
    i, j = 0, len(nums)-1
    result = []
    
    while i <= j:
        if nums[i] ** 2 >= nums[j] ** 2:
            result.insert(0, nums[i] ** 2)
            i += 1
        else:
            result.insert(0, nums[j] ** 2)
            j -= 1
            
    return result


nums = [-4,-1,0,3,10]
print(sortedSquares(nums))

nums = [-7,-3,2,3,11]
print(sortedSquares(nums))
