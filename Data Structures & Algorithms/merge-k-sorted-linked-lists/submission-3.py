# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = head = ListNode()

        cur_min = ListNode(float('inf'))
        curr_in = -1

        pq = []

        for i, khead in enumerate(lists):
            if khead:
                heapq.heappush(pq, (khead.val, i, khead))

        while pq:
            _, i, new_node = heapq.heappop(pq)
            head.next = new_node
            head = head.next
            if new_node.next:
                heapq.heappush(pq, (new_node.next.val, i, new_node.next))

        
        return dummy.next