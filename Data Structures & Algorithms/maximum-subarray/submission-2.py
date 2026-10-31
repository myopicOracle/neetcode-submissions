class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        largest, curr_sum = max(nums), 0

        for num in nums:

            if curr_sum < 0:
                curr_sum = 0

            curr_sum += num 
            largest = max(largest, curr_sum)

        return largest


        # # Brute - Time Limit Exceeded

        # largest = max(nums)

        # for i, num in enumerate(nums):
        #     curr_sum = 0
        #     j = i 
        #     while j < len(nums):
        #         curr_sum += nums[j]
        #         largest = max(largest, curr_sum)
        #         j += 1 

        # return largest

