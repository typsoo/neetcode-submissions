# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = head

        def reverse(h, r_h):
            if not h or not h.next: return None, h

            head_next = h.next
            h.next = None
            prev = h

            while head_next != r_h:
                new_head = head_next.next
                head_next.next = prev
                prev = head_next

                head_next = new_head

            return (h, prev)

        

        cnt = 1
        r_head = None 
        while True:
            if not head and cnt <= k: return res
            if not head and cnt == k + 1:
                end, start = reverse(res, None)
                return start

            if cnt == k + 1: break

            head = head.next
            cnt +=1
        
        l_head, r_head = res, head

        end, start = reverse(l_head, r_head)
        end.next = r_head

        prev = end
        while True:
            l_head = r_head
            for _ in range(k):
                if not r_head: 
                    prev.next = l_head
                    return start
                r_head = r_head.next

            new_end, new_start = reverse(l_head, r_head)
            prev.next = new_start
            prev = new_end

            if not r_head: return start
     





