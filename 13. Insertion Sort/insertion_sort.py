'''
Given an array, sort the numbers using insertion sort technique
input: nums = [8,5,1,6,7]
output: [1,5,6,7,8]
'''

# Time - O(n^2)
# Space - O(1)
def insertionSort(nums):
    for i in range(1, len(nums)):
        j = i
        while (j > 0 and nums[j] < nums[j-1]):
            swap(j, j-1, nums)
            j = j-1
        return nums

def swap(i, j, nums):
    nums[i], nums[j] = nums[j], nums[i]
