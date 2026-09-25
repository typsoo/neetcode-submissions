# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(h):
            if not h or not h.next: return h

            new_head = h.next
            h.next = None
            prev = h

            while new_head:
                next_head = new_head.next
                new_head.next = prev
                prev = new_head

                new_head = next_head
            
            return prev


        n = 0
        s = head
        while head:
            head = head.next
            n +=1
        if n < 3: return head


        rev = s
        rev_prev = None
        for i in range(n//2):
            if i == n//2 - 1: rev_prev = rev
            rev=rev.next
        rev_prev.next = None
        rev = reverse(rev)

        res = curr = ListNode()

        for i in range(n//2):
            res.next = s
            s_next = s.next

            res.next.next = rev

            res = res.next.next
            s = s_next
            rev = rev.next
        
        if n % 2 == 1: 
            res.next = rev




