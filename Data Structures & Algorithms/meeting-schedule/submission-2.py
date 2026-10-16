"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda i: i.end)

        end = -1
        for interval in intervals:
            l, r = interval.start, interval.end
            if end > l:
                return False
            end = r
        return True