'''
Given an array of unsorted integers, find the largest three numbers and return them in an array
input: nums = [141,1,17,-7,-17,-27,18,541,8,7,7]
output: [1,141,541]
'''

# time - O(n) - loop though the entire array
# space - O(1) - no extra space used except an array to store three values

def findThreeLargest(nums):
    result = [None, None, None]
    for num in nums:
        updateLargest(result, num)
    return result
    
def updateLargest(result, num):
    if result[2] is None or num > result[2]:
        shiftAndUpdate(result, num, 2)
    elif result[1] is None or num > result[1]:
        shiftAndUpdate(result, num, 1)
    elif result[0] is None or num > result[0]:
        shiftAndUpdate(result, num, 0)
        
def shiftAndUpdate(result, num, index):
    for i in range(index+1):
        if i == index:
            result[i] = num
        else:
            result[i] = result[i + 1]