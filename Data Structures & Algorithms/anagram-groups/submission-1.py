class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap = {}
        matrix = []

        for s in strs:
            key = "".join(sorted(s))
            if key in hashMap:
                matrix[hashMap[key]].append(s)
            else:
                hashMap[key] = len(matrix)
                matrix.append([s])

        return matrix            


    # Input: strs = ["act","pots","tops","cat","stop","hat"]

    # Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]