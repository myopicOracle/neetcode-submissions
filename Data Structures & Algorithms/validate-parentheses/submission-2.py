class Solution:
    def isValid(self, s: str) -> bool:
        while "()" in s or "{}" in s or "[]" in s:
            s = s.replace("()", "")
            s = s.replace("{}", "")
            s = s.replace("[]", "")
        return s == ""


    # def isValid(self, s: str) -> bool:
        
    #     if len(s) % 2 != 0:
    #         return False

    #     s = self.cleanString(s)        
        
    #     lookup = {"(": ")", "[": "]", "{": "}"}
    #     l, r = 0, len(s) - 1

    #     while l < r:

    #         if lookup[s[l]] != s[r]:
    #             return False

    #         l += 1
    #         r -= 1

    #     return True


    # def cleanString(self, s: str) -> str:
    #     while "()" in s or "{}" in s or "[]" in s:
    #         s = s.replace("()", "")
    #         s = s.replace("{}", "")
    #         s = s.replace("[]", "")
    #     return s        