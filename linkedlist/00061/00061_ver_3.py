# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def count(head):
    length = 0
    scout = head
    while scout.next != None:
        length += 1
        scout = scout.next
    length += 1
    return length, scout

def rotate(head, tail, length, pos_rotate):
    if head.next == None or length == pos_rotate:
        return head

    new_tail = head
    
    for _ in range(pos_rotate):
        new_tail = new_tail.next
        
    tail.next = head
    head = new_tail.next
    new_tail.next = None
    return head

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        length, tail = count(head)
        pos_rotate = length - k % length
        print(length, pos_rotate)
        head = rotate(head, tail, length, pos_rotate - 1)
        return head
