'''
given two arrays, check if the sub array a sequence of nums array
'''

nums = [5, 1, 22, 25, 6, -1, 8, 10]
sub = [1, -1, 6, 10]

'''
Time complexity - O(n) - n is the length of the main array (nums)
Space complexity - O(1) - no extra space used other than a couple of pointers

Explanation
-----------
-> start from the index 0 for both the arrays and see if the value is same
-> if same, then the pointer has to be moved to the next index for both the arrays
-> if not, then only the pointer of main array has to be moved to the next array
-> finally check the count value == length of sub array
'''

def validate_subsequence(nums, sub):
    numIdx = 0
    subIdx = 0
    while numIdx < len(nums) and subIdx < len(sub):
        if nums[numIdx] == sub[subIdx]:
            subIdx = subIdx + 1

        numIdx = numIdx + 1

    return subIdx == len(sub)

print(validate_subsequence(nums, sub))
