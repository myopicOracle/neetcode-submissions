class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            start, end = intervals[i]
            new_start, new_end = newInterval

            if new_end < start:
                res.append(newInterval)
                return res + intervals[i:]

            elif new_start > end:
                res.append(intervals[i])

            else:
                newInterval = [min(start, new_start), max(end, new_end)]

        res.append(newInterval)
        return res


        # res = []
        # i, j = newInterval

        # for start, end in intervals:

        #     if end < i:
        #         res.append([start, end])

        #     elif j < start:
        #         res.append([i, j])

        #     else:
        #         res.append([min(start, i), max(end, j)])

        # return res

