'''
given a binary tree and the target, find the closest value in the binary tree
'''
# Avg case - Time: O(logn) - Space: O(1)
# Worst case - Time: O(n) if the tree has only left or right childs - Space: O(1)

def findClosestVal(root, target):
    # keep a variable to keep track of the closest val
    closest = float("inf")
    currentNode = root
    while currentNode is not None:
        if abs(closest - target) > abs(target - currentNode.value):
            closest = currentNode.value
        if target > currentNode.value:
            currentNode = currentNode.right
        elif target > currentNode.value:
            currentNode = currentNode.left
        else:
            break
    
    return closest