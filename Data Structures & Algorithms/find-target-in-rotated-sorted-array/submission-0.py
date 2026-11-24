class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        for i in range(len(nums)):
            if nums[i] == target:
                return i

        return -1



    # def search(self, nums: List[int], target: int) -> int:
        
    #     l, r = 0, len(nums) - 1

    #     while l < r:
    #         m = l + (r - l) // 2

    #         if nums[m] == target:
    #             return m

    #         if nums[m] > target: 
    #             r = m

    #         else:
    #             l = m + 1

    #     return -1