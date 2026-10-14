class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashMap = {}

        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else: 
                hashMap[num] = 1

        lookup = sorted(((val, key) for key, val in hashMap.items()), reverse=True)

        sorted_hashMap = {key: val for val, key in lookup}

        return list(sorted_hashMap)[:k]


# main = Solution()
# (print(main.topKFrequent([1,2,2,3,3,3], 2)))
# (print(main.topKFrequent([7,7], 1)))