
'''
construct a doubly linked list
'''

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # time: O(1) | space: O(1)
    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    # time: O(1) | space: O(1)
    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    # time: O(1) | space: O(1)
    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        # add the bindings
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    # time: O(1) | space: O(1)
    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.next = node.next
        nodeToInsert.prev=  node
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    # time: O(p) - looping till the position p | space: O(1)
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        currentPosition = 1
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
        # after the end of while loop, there are two cases
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    # time: O(n) | space: O(1)
    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            # we don't want to lose track of our node
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    # time: O(1) | space: O(1)
    def remove(self, node):
        # if node is the head node then point the head to next node
        if node == self.head:
            self.head = self.head.next
        # if node is the tail node then point the tail to prev node
        if node == self.tail:
            self.tail = self.tail.prev
        # we need to change the bindings for nodes which are not head and tail
        # writing a helper function to achieve that
        self.removeNodeBindings(node)

    # time: O(n) | space: O(1)
    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None

    # helper methods to change the pointer bindings
    def removeNodeBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
