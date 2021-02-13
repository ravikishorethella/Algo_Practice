'''
Given a linked list, shift it by k positions
if k is +ve, shift the linked list forward
if k is -ve, shift the linked list backward
'''
# time - O(n) | space - O(1)
def shiftLinkedList(head, k):
    listLength = 1
    tail = head
    while tail is not None:
        tail = tail.next
        listLength += 1

    offset = abs(k) % listLength
    if offset == 0:
        return head

    newTailPosition = listLength - offset if k>0 else offset

    # grab the new head position
    # since we are looping through the linked list, start the index by 1
    newTail = head
    for i in range(1, newTailPosition):
        newTail = newTail.next

    # newTail has the spliced piece
    newHead = newTail.next
    newTail.next = None
    tail.next = head
    return newHead
