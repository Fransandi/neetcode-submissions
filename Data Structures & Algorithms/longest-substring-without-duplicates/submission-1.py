class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        longest = 0

        for right in range(len(s)):
            # Move the left pointer until the current right char is out of the range
            while s[right] in seen:
                seen.remove(s[left])
                left +=1
            
            # Add the right pointer element to the seen set
            seen.add(s[right])
            
            # Update the longest, if needed
            longest = max(longest, right-left+1)

        
        return longest


        