class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mpa  = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            mpa = max(mpa, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return mpa


        # # Brute Force (TLE)
        # mpa = 0

        # # compute the area of each pair of bars

        # i = 0
        # while i < len(heights) - 1:

        #     j = i + 1
        #     while j < len(heights):

        #         area = (j - i) * min(heights[i], heights[j])
        #         mpa = max(mpa, area)

        #         j += 1

        #     i += 1

        # # return the highest area 

        # return mpa