class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            start, end = intervals[i]

            if end < newInterval[0]:
                res.append([start, end])
                # print("if:", res)
                continue
            
            elif newInterval[1] < start:
                res.append(newInterval)
                return res + intervals[i:]

            else:
                newInterval = [min(start, newInterval[0]), max(end, newInterval[1])]
                # print("else:", newInterval)

        res.append(newInterval)
        return res