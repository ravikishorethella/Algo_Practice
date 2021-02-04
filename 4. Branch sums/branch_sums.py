'''
given a binary tree, calculate the sums of all the branches and return a list
'''

# time - O(n)
# space - O(n)

class BinarySearchTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def branchSums(root):
    sums = []
    calculateBranchsums(root, 0, sums)
    return sums

def calculateBranchsums(node, runningSum, sums):
    if node is None:
        return

    newRunningSum = runningSum + node.val

    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return

    calculateBranchsums(node.left, newRunningSum, sums)
    calculateBranchsums(node.right, newRunningSum, sums)