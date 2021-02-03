class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    '''
    Avg case -> time: O(logn) and space: O(1)
    Worst case -> time: O(n) and space: O(1)
    '''
    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self

    '''
    Avg case -> time: O(logn) and space: O(1)
    Worst case -> time: O(n) and space: O(1)
    '''
    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else: 
                return True

        return False

    '''
    Avg case -> time: O(logn) and space: O(1)
    Worst case -> time: O(n) and space: O(1)
    '''
    def remove(self, value, parentNode = None):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                # a root has both left child and right child
                if currentNode.left is not None and currentNode.right is not None:
                    # get the smallest value in the right sub tree
                    currentNode.value = currentNode.right.getMinValue()
                    # once you get the min val, remove the lowest value
                    currentNode.right.remove(currentNode.value, currentNode)
                # root node which doesn't have a parent
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        currentNode.value = None
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None and currentNode.right

                break
        return self

    # function to get the min value in the right sub tree
    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value
