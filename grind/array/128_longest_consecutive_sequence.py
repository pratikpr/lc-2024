# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

def longestConsecutive(nums) -> int:
    nums_set = set(nums)
    longest_sequence = 0
    
    for num in nums_set:
        if num-1 not in nums_set:
            curr_num = num
            curr_streak = 1
            
            while curr_num + 1 in nums_set:
                curr_streak += 1
                curr_num += 1
                
            longest_sequence = max(longest_sequence, curr_streak)
            
    return longest_sequence


nums = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums))

nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))
