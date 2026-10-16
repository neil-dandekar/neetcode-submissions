"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        count = 0
        i = 0
        res = 0
        for s in start:
            count += 1
            while i < len(ends) and ends[i] <= s:
                count -= 1
                i += 1
            res = max(res, count)
        return res


        # [ (0, 2), (0, 3), (1, 4), (3, 5) ]
        # start = [0, 0, 1, 3]
        # end = [2, 3, 4, 5]
        #       x x x
        #   x x x x
        # x x x x
        # x x x
        # 0 1 2 3 4 5 6 7 8 9 10