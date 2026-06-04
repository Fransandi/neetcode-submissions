from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)

        # Edge case, s2 is shorter than s1
        if len_s2 < len_s1:
            return False
        
        count_s1 = Counter(s1)
        count_window = Counter(s2[:len(s1)])
        
        if count_s1 == count_window:
            return True

        for i in range(len(s1), len(s2)):
            count_window[s2[i]] += 1
            count_window[s2[i - len(s1)]] -= 1

            if count_s1 == count_window:
                return True
        
        return False

        