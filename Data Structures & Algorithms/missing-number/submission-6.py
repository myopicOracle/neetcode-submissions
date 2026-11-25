class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for num in range(len(nums) + 1):
            if num not in nums:
                return num



        # prev = 0

        # for i in range(len(nums)):
        #     if (i + 1) != prev:
        #         return (i + 1)
        #     prev = i        


        # seen = {0}

        # for i in range(len(nums)):
        #     if i not in seen:
        #         return i
        #     seen.add(i)
