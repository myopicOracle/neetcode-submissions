class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            self.debug(nums[l:r+1], l, mid, r)

            # in right, so search left
            if nums[mid] < nums[r]:
                r = mid 

            # in left, so search right
            else:
                l = mid + 1

        return nums[l]


        # l, r = 0, len(nums) - 1
        
        # mid = l + (r - l) // 2
        # self.debug(nums[l:r+1], l, mid, r)

        # while l != r:
        #     mid = l + (r - l) // 2

        #     # left sorted portion?
        #     if nums[mid] >= nums[r]:
        #         l = mid
        #         self.debug(nums[l:r+1], l, mid, r)

        #     # right sorted portion?
        #     else:
        #         r = mid
        #         self.debug(nums[l:r+1], l, mid, r)

        # return l


    def debug(self, window, left, middle, right):
        print(f"nums: {window}")
        print(f"left: {left}, mid: {middle}, right: {right}")
        print()


main = Solution()
main.findMin([3,4,5,6,1,2])


        # # Trivial Solution: O(n)
        # return min(nums)
