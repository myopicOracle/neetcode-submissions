class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left, right, longest = 0, 0, 0

        while right < len(s):

            count[s[right]] = count.get(s[right], 0) + 1

            # keeps window valid
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            # update longest valid window
            longest = max(longest, right - left + 1)

            right += 1

        return longest



        # char_index = set(s.split())

        # streak, longest = 1, 0

        # for char in char_index:
        #     copy_s = s[:]

        #     for i, string in enumerate(copy_s[1:]):
        #         replacement = k

        #         while replacement > 0:

        #             if string == s[i - 1] == char:
        #                 streak += 1
        #             else: 
        #                 copy_s[]
        #                 streak += 1
        #                 replacement -= 1

                

