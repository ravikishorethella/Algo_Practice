'''
given an array, find if the given targetVal present in the array
using binary search approach
nums = [2,15,19,24,35,67,72]
target = 67
'''

# recursive approach
# time: O(logn) | space: O(logn) - half of the recursive calls stored in the callstack

def binarySearch(nums, target):
    return binarySearchHelper(nums, target, 0, len(nums)-1)

def binarySearchHelper(nums, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return binarySearchHelper(nums, target, left, mid - 1)
    else:
        return binarySearchHelper(nums, target, mid + 1, right)

# iterative approach
# time - O(logn) | space - O(1)

def binarySearch(nums, target):
    return binarySearchHelper(nums, target, 0, len(nums) - 1)

def binarySearchHelper(nums, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        match = nums[mid]

        if match == target:
            return mid
        elif match > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1