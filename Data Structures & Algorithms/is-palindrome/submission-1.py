class Solution:
    def isPalindrome(self, s: str) -> bool:
        cln_str = ""

        for char in s: 
            if char.isalnum(): cln_str += char.lower()

        return cln_str == cln_str[::-1]
        
    
    #     cleaned_string = self.clean_string(s)

    #     end = start = len(cleaned_string) // 2
    #     if len(cleaned_string) % 2 != 0: 
    #         start += 1

    #     return cleaned_string[:end] == cleaned_string[start:][::-1]


    # def clean_string(self, s: str) -> str:
    #     cleaned_list = [char for char in s.lower() if char.isalnum()]
    #     return "".join(cleaned_list)


# main = Solution()
# print(main.isPalindrome("Was it a car or a cat I saw?"))
# print(main.isPalindrome("tab a cat"))
