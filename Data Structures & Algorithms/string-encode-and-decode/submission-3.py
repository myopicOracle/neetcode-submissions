class Solution:

    def encode(self, strs: List[str]) -> str:
        new_string = ""

        for s in strs:
            new_string += f"{len(s)}#{s}"

        return new_string 

    def decode(self, s: str) -> List[str]:
        res_list = []

        i = 0
        while i < len(s):

            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            
            word = s[j + 1 : j + 1 + length]
            res_list.append(word)
            
            i = j + 1 + length
            
        return res_list


# main = Solution()
# output = main.encode(["Hello","World"])
# main.decode(output)