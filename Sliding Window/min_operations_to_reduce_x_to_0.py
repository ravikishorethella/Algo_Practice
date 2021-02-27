
'''
You are given an integer array nums and an integer x. In one operation, 
you can either remove the leftmost or the rightmost element from the array nums 
and subtract its value from x. Note that this modifies the array for future operations.
Return the minimum number of operations to reduce x to exactly 0 if it's possible, 
otherwise, return -1.
'''
# time - O(n)
# space - O(1)

def minOperations(self, nums: List[int], x: int) -> int:
    n = len(nums)
    target = sum(nums) - x
    start = 0
    window_sum = 0
    size = -1
    
    for end, num in enumerate(nums):
        window_sum = window_sum + num
        
        while start < n and window_sum > target:
            window_sum = window_sum - nums[start]
            start = start + 1
        
        if window_sum == target:
            size = max(size, end - start + 1)
            
    return -1 if size < 0 else n - size
