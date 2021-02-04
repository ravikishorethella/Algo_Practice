'''
given a tree, output a list by performing the DFS

            A
          /   \ 
         B     C
        / \   /  \
       D   E F    G

outut list = [ABDECFG]
'''

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def addChild(self, name):
        self.children.append(Node(name))

    # time: O(v+e) - vertices + edges
    # space: O(v)
    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array
