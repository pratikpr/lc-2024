# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

def merge(nums1, m: int, nums2, n: int) -> None:
    curr = len(nums1)-1
    i, j = m-1, n-1
    
    while i >= 0 and j >= 0:
        if nums1[i] >= nums2[j]:
            nums1[curr] = nums1[i]
            curr -= 1; i -= 1
        else:
            nums1[curr] = nums2[j]
            curr -= 1; j -= 1
    
    if i <= 0:
        while j >= 0:
            nums1[curr] = nums2[j]
            curr -= 1; j -= 1
    else:
        while i >= 0:
            nums1[curr] = nums1[i]
            curr -= 1; i -= 1
            
    print(nums1)
    

nums1 = [0]; m = 0; nums2 = [1]; n = 1
merge(nums1, m, nums2, n)

nums1 = [1,2,3,0,0,0]; m = 3; nums2 = [2,5,6]; n = 3
merge(nums1, m, nums2, n)

nums1 = [1]; m = 1; nums2 = []; n = 0
merge(nums1, m, nums2, n)
