import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prod_all = math.prod(nums)

        if 0 in nums:
            for i in range (len(nums)):
                if nums[i] != 0:
                    res.append(0)
                else:
                    ex_self = nums[:]
                    ex_self.pop(i)
                    res.append(math.prod(ex_self))

        else:
            for i in range(len(nums)):
                ex_self = prod_all // nums[i]
                res.append(ex_self)

        return res
        

        # res = []

        # for i in range(len(nums)):
        #     new_list = nums[:]
        #     new_list.pop(i)
        #     res.append(math.prod(new_list))

        # return res