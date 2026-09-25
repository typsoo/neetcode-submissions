"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        arr = []
        for ob in intervals:
            arr.append([ob.start, ob.end])

        if not arr: return True
        arr.sort()
        ps, pe = arr[0]
        for i in range(1, len(arr)):
            s, e = arr[i]
            if pe > s:
                return False
            else:
                ps, pe = s, e
        
        return True