'''
Given a binary search tree, validate whether it is a valid BST or not
'''
# time - O(N) - N nodes
# space - O(d) - d is the depth of the tree because, d callstacks for recersively solving

def validateBst(tree):
    return validateBstHelper(tree, float('-inf'), float('inf'))

def validateBstHelper(tree, minValue, maxValue):
    # check if we are at the leaf, i.e, at the bottom of the branch
    if tree is None:
        return True

    # if we are at the actual node
    if tree.value < minValue or tree.value >= maxValue:
        return False
    
    # if our node comes to this point then we need to check the left subtree
    leftIsValid = validateBstHelper(tree.left, minValue, tree.value)
    return leftIsValid and validateBstHelper(tree.right, tree.value, maxValue)