# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

def rotate(nums, k: int) -> None:
    n = len(nums)
    k = k % n
    nums.reverse()
    
    start, end = 0, k-1
    while start <= end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1; end -= 1
        
    start, end = k, n-1
    while start <= end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1; end -= 1
        
def rotateIdx(nums, k):
    n = len(nums)
    k %= n
    
    start = 0; count = 0
    
    while count < n:
        cur, prev = start, nums[start]
        while True:
            next = (cur + k) % n
            nums[next], prev = prev, nums[next]
            cur = next
            count += 1
            
            if start == cur:
                break
        start += 1
        
        
nums = [1,2,3,4,5,6,7]; k = 3
rotateIdx(nums, k)
print(nums)