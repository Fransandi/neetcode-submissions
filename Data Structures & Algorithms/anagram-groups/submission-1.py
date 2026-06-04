class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = dict()

        for word in strs:
            key = [0] * 26
            for char in word:
                key[ord(char) - ord('a')] += 1
            key = tuple(key)
            
            if key not in dic:
                dic[key] = []
            dic[key].append(word)

        return [dic[key] for key in dic]
                

