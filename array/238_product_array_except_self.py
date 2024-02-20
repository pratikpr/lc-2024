# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

def productExceptSelf(nums):
    result = [1] * len(nums)
    product_prefix = 1
    
    for i in range(len(nums)):
        result[i] *= product_prefix
        product_prefix *= nums[i]
    print(result)
        
    product_prefix = 1
    for i in range(len(nums)-1, -1, -1):
        result[i] *= product_prefix
        product_prefix *= nums[i]
        
    return result

nums = [1,2,3,4]
print(productExceptSelf(nums))

nums = [-1,1,0,-3,3]
print(productExceptSelf(nums))