class Solution:
    def canJump(self, nums: List[int]) -> bool:
        threshold = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= threshold:
                threshold = i

        return True if threshold == 0 else False


        # reachable = 0

        # for current in range(len(nums)):

        #     if current > reachable:
        #         return False

        #     jump = current + nums[current]
        #     reachable = max(reachable, jump)

        #     if reachable >= len(nums) - 1:
        #         return True

        # return True


        # i = 0

        # while i < len(nums):

        #     jump = nums[i]

        #     i += jump 

        #     if i == last_index:
        #         return True

        # return false