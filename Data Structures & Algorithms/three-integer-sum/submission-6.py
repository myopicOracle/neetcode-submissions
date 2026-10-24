class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums[i] + nums[j] == -nums[k]

        nums.sort()
        res = []

        for i, num in enumerate(nums):
            if num > 0:
                break

            if i > 0 and num == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                three_sum = num + nums[l] + nums[r]

                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res


        ## Brute Force 1 (too slow)
        ## pseudo
        # given: nums[i] + nums[j] + nums[k] == 0 -> nums[i] + nums[j] == -nums[k] -> target = -nums[k]
        # store the sum and values of all possible pairs
        # for every pair of numbers in nums that sum to -nums[k]
        # append the pair + nums[k]
        # return all triplets

        # i, j = 0, len(nums) - 1
        # nums.sort()
        # hash_map = {}

        # # build 2sum dict
        # while j > 0:
        #     while i < j:
        #         two_sum = nums[i] + nums[j]

        #         if two_sum not in hash_map:
        #             hash_map[two_sum] = []
                    
        #         hash_map[two_sum].append((i, j))
        #         i += 1
            
        #     i = 0
        #     j -= 1

        # res_set = set()

        # # match stored 2sum dict to locate k
        # for k, num in enumerate(nums):
        #     target = -num  
            
        #     if target in hash_map:
        #         for i1, j1 in hash_map[target]:
        #             if k != i1 and k != j1:
        #                 triplet = tuple(sorted([nums[i1], nums[j1], nums[k]]))
        #                 res_set.add(triplet)

        # return [list(triplet) for triplet in res_set]
       
