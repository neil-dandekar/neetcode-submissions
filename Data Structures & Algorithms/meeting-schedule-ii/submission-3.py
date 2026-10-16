"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        i = 0
        active = 0
        res = 0
        for s in starts:
            active += 1
            while i < len(ends) and ends[i] <= s:
                active -= 1
                i += 1
            res = max(res, active)
        return res