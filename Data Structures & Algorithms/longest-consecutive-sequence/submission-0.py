class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        helper = sorted(set(nums))

        segment = []
        for i in range(len(helper)):
            gap = helper[i] + 1
            bound = len(helper) - 1
            
            segment.append(helper[i])
            
            if len(segment) > longest:
                longest = len(segment)
            
            if (i < bound) and ( gap != helper[i + 1]): 
                segment = []    
            
        return longest


# main = Solution()
# main.longestConsecutive([2,20,4,10,3,4,5])
# main.longestConsecutive([0,3,2,5,4,6,1,1])