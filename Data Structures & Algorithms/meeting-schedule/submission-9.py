"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i : i.start)

        if len(intervals) == 0:
            return True

        prev_end = intervals[0].end

        for i in intervals[1:]:
            start, end = i.start, i.end

            if i.start < prev_end:
                return False

            prev_end = i.end

        return True