class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for item in strs:
            key = ''.join(sorted(list(item)))
            if key not in dic:
                dic[key] = [item]
            else:
                dic[key].append(item)
        return list(dic.values())

        