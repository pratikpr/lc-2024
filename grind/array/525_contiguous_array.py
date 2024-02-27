# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

def findMaxLength(nums) -> int:
    freq = {}
    freq[0] = 0
    running_sum = [0]
    
    for n in nums:
        if n == 0:
            running_sum.append(running_sum[-1] - 1)
        else:
            running_sum.append(running_sum[-1] + 1)
    
            
    longest = 0
    for i in range(1,len(running_sum)):
        if running_sum[i] in freq:
            cur = i - freq[running_sum[i]]
            longest = max(longest, cur)
        else:
            freq[running_sum[i]] = i
            
    return longest


nums = [0, 0, 1, 0, 0, 0, 1, 1]
print(findMaxLength(nums))

nums = [1,0,1,1,0,1,0,0,0,1]
print(findMaxLength(nums))

nums = [0,1]
print(findMaxLength(nums))

nums = [0,1,0]
print(findMaxLength(nums))