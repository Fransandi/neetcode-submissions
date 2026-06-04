class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Edge case: empty list
        if not len(s):
            return 0

        count = dict()
        i, j = 0, 0
        longest = 0

        while i <= j and j < len(s):
            char = s[j]

            if char not in count:
                count[char] = 1
                longest = max(longest, j-i+1)
                j += 1
            else:
                while char in count and i < j:
                    count[s[i]] -=1
                    if count[s[i]] == 0:
                        del count[s[i]]
                    i += 1

        return longest


        