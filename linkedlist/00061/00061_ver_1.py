# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def count(head):
    if head.next == None:
        return 1
    length = 0
    while head.next != None:
        head = head.next
        length += 1
    return length

def rotate(head):
    if head.next == None:
        return head
    zoombie = ListNode(0, head)
    tail = head
    new_tail = zoombie
    while tail.next != None:
        tail = tail.next
        new_tail = new_tail.next
    new_tail.next = None
    tail.next = head
    head = tail
    return head

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        for index in range(k):
            head = rotate(head)
            
        return head
