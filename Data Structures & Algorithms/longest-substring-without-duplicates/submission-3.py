class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left, right, longest = 0, 0, 0

        while right < len(s):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            longest = max(longest, right - left + 1)

            right += 1

        return longest



        # seen = set()
        # l, longest = 0, 0

        # for r in range(len(s)):
        #     while s[r] in seen:
        #         seen.remove(s[l])
        #         l += 1
        #     seen.add(s[r])
        #     longest = max(longest, r - l + 1)

        # return longest 


        # longest = 0
        # streak = 0

        # seen = set()

        # for char in s:

        #     if char in seen:
        #         seen = set()
        #         streak = 0
        #         continue
        #     else:
        #         seen.add(char)
        #         streak += 1
        #         longest = max(longest, streak)

        # return longest