'''
Given an array, sort the numbers using bubble sort technique
input: nums = [8,5,1,6,7]
output: [1,5,6,7,8]
'''

# Time - O(n^2)
# Space - O(1)
def bubbleSort(nums):
    isSorted = False
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range(len(nums)-1):
            if(nums[i] > nums[i+1]):
                swap(i, i+1, nums)
                isSorted = False
        counter = counter + 1
    return nums

def swap(i, j, nums):
    nums[i], nums[j] = nums[j], nums[i]