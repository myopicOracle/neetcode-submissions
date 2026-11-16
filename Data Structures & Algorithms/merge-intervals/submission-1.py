class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        res = [intervals[0]]

        prev_start, prev_end = intervals[0][0], intervals[0][1]
        for start, end in intervals[1:]:

            if start > prev_end:
                res.append([start, end])
                prev_start, prev_end = start, end

            else:
                res[-1] = [min(prev_start, start), max(prev_end, end)]
                prev_start, prev_end = res[-1]

        return res