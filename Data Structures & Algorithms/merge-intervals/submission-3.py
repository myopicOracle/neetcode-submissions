class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        
        # only 2 possible cases since sorted
        for start, end in intervals[1:]:

            # no overlap
            if start > res[-1][1]:
                res.append([start, end])

            # overlap
            else:
                res[-1][1] = max(res[-1][1], end)
            
        return res


# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         intervals.sort()
#         res = [intervals[0]]
        
#         prev_start, prev_end = intervals[0]
#         for start, end in intervals[1:]:

#             if start > prev_end:
#                 res.append([start, end])
#                 prev_start, prev_end = start, end

#             else:
#                 res[-1] = [min(prev_start, start), max(prev_end, end)]
#                 prev_start, prev_end = res[-1]

#         return res
