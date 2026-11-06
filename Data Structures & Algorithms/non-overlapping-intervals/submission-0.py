class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i : i[0])
        count = 0

        last_end = intervals[0][1]
        for start, end in intervals[1:]:

            if start >= last_end:
                last_end = end
            else:
                count += 1
                last_end = min(last_end, end)
                
        return count