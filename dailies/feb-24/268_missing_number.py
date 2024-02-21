# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

def missingNumber(nums) -> int:
        _sum = sum(nums)
        n = len(nums)
        n_sum = (n * (n+1))//2
        # print(n_sum, _sum)
        return n_sum - _sum
    
nums = [9,6,4,2,3,5,7,0,1]
print(missingNumber(nums))

nums = [3,0,1]
print(missingNumber(nums))
