class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in hashmap:
                return [hashmap[diff], i]

            hashmap[num] = i 

        # nums[i] + nums[j] == target
        # nums = [3,4,5,6], target = 7

        # 3 + 4
        # 3 + 5
        # 3 + 6

        # 4 + 5 
        # 4 + 6

        # 5 + 6

        ## Brute Force
        # for i in range(len(nums) - 1):

        #     for j in range(i + 1, len(nums)):

        #         if nums[i] + nums[j] == target:
        #             return sorted([i, j])
