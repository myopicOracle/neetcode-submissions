class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for s in strs:
            key = "".join(sorted(s))

            if key in hashmap:
                hashmap[key].append(s)
            else:
                hashmap[key] = [s]

        return list(hashmap.values())


        # hashMap = {}

        # for s in strs:
        #     key = "".join(sorted(s))

        #     if key in hashMap:
        #         hashMap[key].append(s)
        #     else:
        #         hashMap[key] = [s]

        # return list(hashMap.values())


        # hashMap = {}
        # matrix = []

        # for s in strs:
        #     key = "".join(sorted(s))
        #     if key in hashMap:
        #         matrix[hashMap[key]].append(s)
        #     else:
        #         hashMap[key] = len(matrix)
        #         matrix.append([s])

        # return matrix            


    # Input: strs = ["act","pots","tops","cat","stop","hat"]

    # Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]