# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head = ListNode()

        ad = 0
        while l1 and l2:
            val = l1.val + l2.val + ad
            head.next = ListNode(val%10)
            head = head.next

            l1 = l1.next
            l2 = l2.next

            ad = 1 if val >= 10 else 0

        if not l1 and not l2:
            if ad:
                head.next = ListNode(ad)


        elif l1:
            while l1:
                val = l1.val + ad
                head.next = ListNode(val%10)
                head = head.next

                l1 = l1.next
                ad = 1 if val >= 10 else 0
            if ad == 1: head.next = ListNode(1)



        else:
            while l2:
                val = l2.val + ad
                head.next = ListNode(val%10)
                head = head.next

                l2 = l2.next
                ad = 1 if val >= 10 else 0
            if ad == 1: head.next = ListNode(1)


        return dummy.next
        
