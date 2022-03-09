# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        zoombie = ListNode(0, head)
        scout = zoombie
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                scout.next = head.next
            else:
                scout = scout.next
            head = head.next
        return zoombie.next

