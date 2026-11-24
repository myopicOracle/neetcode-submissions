import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for _ in nums]

        # pass 1, traverse right, update every num for product left_of
        left_of = 1
        for i in range(len(nums)):
            # print(left_of)
            res[i] *= left_of
            left_of *= nums[i]


        # pass 2, traverse left, update every num for product right_of
        right_of = 1
        for i in range(len(nums) - 1, -1, -1):
            # print(right_of)
            res[i] *= right_of
            right_of *= nums[i]

        return res





        # res = [1] * len(nums)

        # prefix = 1
        # for i in range(len(nums)):
        #     res[i] = prefix
        #     prefix *= nums[i]
            
        # postfix = 1
        # for i in range(len(nums) - 1, -1, -1):
        #     res[i] *= postfix
        #     postfix *= nums[i]

        # return res
        
        
        # res = []
        # prod_all = math.prod(nums)

        # if 0 in nums:
        #     for i in range (len(nums)):
        #         if nums[i] != 0:
        #             res.append(0)
        #         else:
        #             ex_self = nums[:]
        #             ex_self.pop(i)
        #             res.append(math.prod(ex_self))

        # else:
        #     for i in range(len(nums)):
        #         ex_self = prod_all // nums[i]
        #         res.append(ex_self)

        # return res
        

        # res = []

        # for i in range(len(nums)):
        #     new_list = nums[:]
        #     new_list.pop(i)
        #     res.append(math.prod(new_list))

        # return res





