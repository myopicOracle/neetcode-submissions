class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r = 0, len(numbers) - 1

        while l < r:
            curr_sum = numbers[l] + numbers[r]

            if curr_sum > target:
                r -= 1
            elif curr_sum < target: 
                l += 1
            else:
                return [l + 1, r + 1]


        # hashMap = {}

        # for i, num in enumerate(numbers):
        #     diff = target - num

        #     if diff in hashMap:
        #         return sorted([i + 1, hashMap[diff] + 1])
        #     else:
        #         hashMap[num] = i
