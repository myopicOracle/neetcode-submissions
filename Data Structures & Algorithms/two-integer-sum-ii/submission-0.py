class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        hashMap = {}

        for i, num in enumerate(numbers):
            diff = target - num

            if diff in hashMap:
                return sorted([i + 1, hashMap[diff] + 1])
            else:
                hashMap[num] = i
