"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)

        heap = []

        for inter in intervals:
            s, e = inter.start, inter.end
            if not heap:
                heapq.heappush(heap, e)
                continue

            if s >= heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, e)
            else:
                heapq.heappush(heap, e)



        return len(heap)

