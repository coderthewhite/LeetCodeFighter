class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotate(head):
    if not head:
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

def traverse(head):
    while head:
        print(head.val, end="--->")
        head = head.next
    print("None")

if __name__ == '__main__':
    head = ListNode(1, None)
    scout = head
    for value in range(2, 6):
        scout.next = ListNode(value, None)
        scout = scout.next
    traverse(head)
    for index in range(2):
        head = rotate(head)
    traverse(head)
    
    
