'''
given a binary tree, calculate the total node depths 
'''

# recursive approach
# time: O(n) | space: O(h) - call stack of the recursive will be the almost the height of the tree
# the recursive approach has to go thorough all the branches 

def calculateNodeDepth(root, depth = 0):
    if root is None:
        return 0
    
    return 1 + calculateNodeDepth(root.left, depth + 1) + calculateNodeDepth(root.right, depth + 1)


# iterative approach
# time: O(n) | space: O(h) - the stack we create will have to store the elements (cont')
# will almost be the height of the tree

def calculateNodeDepth(root):
    totalSum = 0
    # we push the root node and its depth to the stack
    stack = [{"node": root, "depth": 0}]
    while len(stack) > 0:
        nodeInfo = stack.pop()
        node, depth = nodeInfo["node"], nodeInfo["depth"]
        # if the node is Null, continue the loop
        if node is None:
            continue
        # calcualte the totalSum
        totalSum = totalSum + depth
        # append the left child and right child into the stack
        stack.append({"node": root.left, "depth": depth + 1})
        stack.append({"node": root.right, "depth": depth + 1})
        
    return totalSum
