# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

def threeSum(nums):
    nums.sort()
    result = []
    
    for start in range(len(nums)-2):
        if start > 0 and nums[start] == nums[start-1]:
            continue
        i,j = start+1, len(nums)-1
        target = -nums[start]
        
        while i < j:
            
                
            _sum = nums[i] + nums[j]
            if _sum == target:
                result.append([nums[start], nums[i], nums[j]])
                i += 1; j -= 1
                while i < j and nums[i] == nums[i-1]:
                    i += 1
            elif _sum > target:
                j -= 1
            else:
                i += 1
                
    return result


nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))

nums = [0,0,0]
print(threeSum(nums))

nums = [0,1,1]
print(threeSum(nums))

nums = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
print(threeSum(nums))
