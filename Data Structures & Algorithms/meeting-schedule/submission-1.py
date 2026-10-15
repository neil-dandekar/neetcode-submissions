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
        intervals.sort(key=lambda i: (i.start, i.end))

        end = intervals[0].end
        for interval in intervals[1:]:
            l, r = interval.start, interval.end
            if end > l:
                return False
            end = r
        return True