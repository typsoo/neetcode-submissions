# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        s = head

        l = 0
        while head:
            head = head.next
            l += 1

        if l == n: return s.next

        res = s
        for _ in range(l - n - 1):
            s = s.next
        s.next = None if n == 1 else s.next.next

        return res