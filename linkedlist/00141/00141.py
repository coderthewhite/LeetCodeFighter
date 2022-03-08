# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slower = faster = head
        
        if not head:
            return False
        
        while faster.next and faster.next.next:
            slower = slower.next
            faster = faster.next.next
            if slower == faster:
                return True
        return False
