'''
Given an array, sort the numbers using selection sort technique
input: nums = [8,5,1,6,7]
output: [1,5,6,7,8]
'''

# Time - O(n^2)
# Space - O(1)
def selectionSort(nums):
    currentIndex = 0 # first num in the unsorted list
    while currentIndex < len(nums) - 1:
        smallestIndex = currentIndex
        for i in range(currentIndex+1, len(nums)):
            if nums[smallestIndex] > nums[i]:
                smallestIndex = i
        swap(currentIndex, smallestIndex, nums)
        currentIndex = currentIndex + 1
    return nums

def swap(i, j, nums):
    nums[i], nums[j] = nums[j], nums[i]