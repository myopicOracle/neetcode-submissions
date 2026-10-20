class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        deduped = set(nums)
        longest = 0
        streak = 1

        for num in deduped:

            # for each first element in group
            if (num - 1) not in deduped: 

                curr_num = num
                # check each consecutive until none left
                while (curr_num + 1) in deduped:
                    # increment tally for each consecutive
                    streak += 1 
                    curr_num += 1

                longest = max(longest, streak)
                streak = 1

        return longest


        ## Brute, O(nlogn)

        # longest = 0

        # arr = sorted(set(nums))

        # segment = []
        # for i in range(len(arr)):
        #     gap = arr[i] + 1
        #     bound = len(arr) - 1
            
        #     segment.append(arr[i])
            
        #     if len(segment) > longest:
        #         longest = len(segment)
            
        #     if (i < bound) and ( gap != arr[i + 1]): 
        #         segment = []    
            
        # return longest


# main = Solution()
# main.longestConsecutive([2,20,4,10,3,4,5])
# main.longestConsecutive([0,3,2,5,4,6,1,1])