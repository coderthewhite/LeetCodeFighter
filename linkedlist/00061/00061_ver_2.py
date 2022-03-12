# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def count(head):
    length = 0
    scout = ListNode(0, head)
    while scout.next != None:
        length += 1
        scout = scout.next
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
        length = count(head)
        num_rotate = k % length
        print(length)
        for index in range(num_rotate):
            head = rotate(head)
        return head