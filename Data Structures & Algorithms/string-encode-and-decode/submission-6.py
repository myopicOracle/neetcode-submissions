class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for s in strs:
            encoded_string += f"{len(s)}#{s}"
        
        return encoded_string


    def decode(self, s: str) -> List[str]:
        res = []
        i, j = 0, 0

        # find start index and length of each fragment

        while i < len(s):

            if s[i] == "#":
                length = int(s[j:i])

                start = i + 1
                end = start + length

                fragment = s[start:end]
                res.append(fragment)

                j = i = end
                
            else:
                i += 1

        return res
        

# def encode(self, strs: List[str]) -> str:
#     encoded_string = ""

#     for s in strs:
#         encoded_string += f"{len(s)}#{s}"
    
#     return encoded_string


# def decode(self, s: str) -> List[str]:
#     res = []
#     i = 0

#     # handle edge cases

#     if s == "0#":
#         return res + [""]

#     if s == "1##": 
#         return res + ["#"]

#     # find start index and length of each fragment

#     while i < len(s):

#         if s[i] == "#":
#             start = i + 1
#             length = int(s[i - 1])
#             end = start + length
#             fragment = s[start:end]
#             res.append(fragment)

#         i += 1

#     return res


# def encode(self, strs: List[str]) -> str:
#     new_string = ""

#     for s in strs:
#         new_string += f"{len(s)}#{s}"

#     return new_string 

# def decode(self, s: str) -> List[str]:
#     res_list = []

#     i = 0
#     while i < len(s):

#         j = i
#         while s[j] != "#":
#             j += 1
        
#         length = int(s[i:j])
        
#         word = s[j + 1 : j + 1 + length]
#         res_list.append(word)
        
#         i = j + 1 + length
        
#     return res_list


# class Solution:

#     def encode(self, strs: List[str]) -> str:
#         res = []
#         for s in strs:
#             res.append(str(len(s)))
#             res.append("#")
#             res.append(s)
#         return "".join(res)

#     def decode(self, s: str) -> List[str]:
#         res = []
#         i = 0

#         while i < len(s):
#             j = i
#             while s[j] != '#':
#                 j += 1
#             length = int(s[i:j])
#             i = j + 1
#             j = i + length
#             res.append(s[i:j])
#             i = j

#         return res


# main = Solution()
# output = main.encode(["Hello","World"])
# main.decode(output)