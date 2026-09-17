from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0 or not head.next:
            return head
        old_tail = head
        length = 1
        while old_tail.next:
            old_tail = old_tail.next
            length += 1
        old_tail.next = head
        new_tail_idx = length - (k % length)
        new_tail = head
        for _ in range(new_tail_idx - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head