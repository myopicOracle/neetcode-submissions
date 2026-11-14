"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # [[start_1,end_1],[start_2,end_2],...] (start_i < end_i)

        if not intervals:
            return True

        intervals.sort(key = lambda i : i.start)

        helper_arr = [intervals[0]]

        prev_end = helper_arr[0].end

        for i in intervals[1:]:
            if i.start < prev_end:
                return False
            else:
                prev_end = i.end

        return True
