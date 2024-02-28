# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

def subarraySum(nums, k: int) -> int:
    cum_sum = [0]
    count = 0
    
    for n in nums:
        cum_sum.append(cum_sum[-1]+n)
    # print(cum_sum)
    
    for i in range(len(cum_sum)):
        for j in range(i+1, len(cum_sum)):
            if cum_sum[j] - cum_sum[i] == k:
                print(i, j)
                count += 1
                
    return count


def subarraySum(nums, k: int) -> int:
    count, _sum = 0, {}
    curr_sum = 0
    _sum[0] = 1
    
    for i in range(len(nums)):
        curr_sum += nums[i]
        if curr_sum-k in _sum:
            count += _sum[curr_sum-k]
        if curr_sum not in _sum:
            _sum[curr_sum] = 0        
        _sum[curr_sum] += 1
        
    return count
    
    
nums = [1,2,3]; k = 3
print(subarraySum(nums, k))

nums = [1,1,1]; k = 2
print(subarraySum(nums, k))
