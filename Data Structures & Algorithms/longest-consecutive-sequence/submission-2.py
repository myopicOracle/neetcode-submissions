class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        deduped = set(nums)
        longest, streak = 0, 1

        for num in deduped:

            # find start of streak
            if (num - 1) not in deduped:
                curr_num = num

                # add 1 for each consec
                while (curr_num + 1) in deduped:
                    streak += 1
                    curr_num += 1

                longest = max(streak, longest)
                streak = 1

        return longest


        # deduped = set(nums)
        # longest, streak = 0, 0

        # for num in nums:

        #     # find start of streak
        #     while (num - 1) not in deduped:
        #         curr_num = num

        #         # add 1 for each consec
        #         while (curr_num + 1) in deduped:
        #             streak += 1
        #             curr_num += 1

        #         longest = max(streak, longest)

        # return longest


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