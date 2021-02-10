'''
Given an array, find the tripelts which sums up to the target
'''
# time - O(n^2)
# space - O(n) - at most, we will have to store all the values from array into triplets
def threeNumSum(array,target):
    # using a two pointer technique so, we need to sort the array
    array.sort()
    triplets = []
    for i in range(len(array)):
        left = i+1
        right = len(array)-1
        if i == 0 or array[i-1] != array[i]:
            while left < right:
                currentSum = array[i] + array[left] + array[right]
                if currentSum == target:
                    triplets.append([array[i], array[left], array[right]])
                    left = left + 1
                    right = right - 1
                    while left < right and array[left] == array[left - 1]:
                        left = left + 1
                elif currentSum < target:
                    left = left + 1
                elif currentSum > target:
                    right = right - 1
    return triplets

print(threeNumSum([-1,0,1,2,-1,-4], 0))
