'''
calculate the product sum of the given array
'''

# time - O(n) - all the elements in the array including the nested array elements
# space - O(D) 

def productSum(array, multiplier = 1):
    totalSum = 0
    for element in array:
        if type(element) is list:
            totalSum += productSum(element, multiplier + 1)
        else:
            totalSum += element
    return totalSum * multiplier
