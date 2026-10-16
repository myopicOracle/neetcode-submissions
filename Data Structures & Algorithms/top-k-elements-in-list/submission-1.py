class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        tuple_list = []
        for key, val in count.items():
            tuple_list.append((val, key))

        return [item[1] for item in sorted(tuple_list, reverse=True)[:k]]
