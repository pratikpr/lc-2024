# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

def majorityElement(nums):
    nums.sort()
    return nums[len(nums)//2]


def majorityElementHash(nums):
    n = len(nums)
    freq = {}
    
    for num in nums:
        if num not in freq:
            freq[num] = 0
        freq[num] += 1
        
    print("------")
    print(freq)
        
    for k, v in freq.items():
        if v >= n/2:
            return k
    
    
        
    return -1    

nums = [6,5,5]
print(majorityElementHash(nums))

nums = [3,2,3]
print(majorityElementHash(nums))