"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        arr = []
        for ob in intervals:
            arr.append([ob.start, ob.end])

        if not arr: return 0
        arr.sort()
        heap = [arr[0][1]]


        cnt = 1
        for i in range(1, len(arr)):
            s, e = arr[i]
            if heap[0] > s:
                heapq.heappush(heap, e)
                cnt += 1
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, e)
            
        
        return cnt