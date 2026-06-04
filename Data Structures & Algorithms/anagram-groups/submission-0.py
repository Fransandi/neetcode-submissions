class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = dict()

        for word in strs:
            key = "".join(sorted(word))
            if key not in dic:
                dic[key] = []
            dic[key].append(word)

        return [dic[key] for key in dic]
                