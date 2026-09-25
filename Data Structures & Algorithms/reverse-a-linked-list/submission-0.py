# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        new_head = head.next
        head.next = None
        prev = head

        while new_head:
            nn = new_head.next
            new_head.next = prev
            prev = new_head
            new_head = nn
        
        return prev

        