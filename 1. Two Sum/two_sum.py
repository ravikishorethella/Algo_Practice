'''
given an array, return the indices of two numbers who sum upto to the target
nums = [1,3,5,7,6]
target = 9 or 12 or whatever
'''

nums = [1,3,5,7,6]
target = 12

# solution 1 (iterative approach)
'''
-> time complexity O(n^2) - nested loops
-> space complexity O(1) - as we are not using any extra space

 explanation
--------------

-> start i with the first index and j with i+1 till length - 1 of the list
-> check if nums[i] + nums[j] == target
'''
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(1, len(nums) - 1):
            if nums[i] + nums[j] == target:
                return [i, j]

print(two_sum(nums, target))


# solution 2 (using dictionary)
'''
-> time complexity - O(n) - looping through the list just once
-> space complexity - O(n) - using dictionary to use the elements

 explanation 
-------------
-> i + j = target and j = target - i
-> loop through the list and find the difference with target and store the result in the dictionary
-> if for any number in the remaining list == the diff in the dictionary then bang! get those indices 

'''
def two_sum(nums, target):
    store = {}
    for index, num in enumerate(nums):
        if num in store:
            return [store[num], index]
        else:
            store[target-num] = index

print(two_sum(nums, target))


# solution 3 (using two pointers)
'''
-> time complexity - O(nlogn) - as we are looping through the whole list and using a sorting algorithm
-> space complexity - O(1) - we are not using any extra space

** The input list has to be a sorted list

 explanation
 -----------
-> use a pointer from index 0 and second pointer from the end of the list
-> calculate the sum of the values at those two indices and 
-> if the target is greater than the sum then move the left pointer to next index
-> if the target is lesser than the sum then move the right pointer to the prev index
-> if it is equal then return those indices
'''

def two_sum(nums, target):
    nums.sort()
    i = 0
    j = len(nums) - 1
    while(i < j):
        calc_sum = nums[i] + nums[j]
        if target == calc_sum:
            return [i, j]
        elif target > calc_sum:
            i = i + 1
        else:
            j = j - 1
    
    return [i, j]

print(two_sum(nums, target))