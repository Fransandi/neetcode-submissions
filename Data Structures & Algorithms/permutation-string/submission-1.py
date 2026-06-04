class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # Edge case: s2 is shorter than s1
        if len(s2) < len(s1):
            return False

        # Count the chars of s1
        s1_count = {}
        for c in s1:
            if c not in s1_count:
                s1_count[c] = 0
            s1_count[c] += 1

        print('s1_count', s1_count)

        # Initialize the count of s2
        s2_count = {}
        for i in range(len(s1)):
            c = s2[i]
            if c not in s2_count:
                s2_count[c] = 0
            s2_count[c] += 1

        print('s2_count', s2_count)

        # If at any point the counts are the same, True
        if s1_count == s2_count:
            return True

        # Iterate all chars, updating the count
        for i in range(len(s1), len(s2)):
            new_c = s2[i]
            old_c = s2[i - len(s1)]

            if new_c not in s2_count:
                s2_count[new_c] = 0
            s2_count[new_c] += 1

            s2_count[old_c] -= 1
            if s2_count[old_c] == 0:
                del s2_count[old_c]

            print('s2_count', s2_count)

            # If at any point the counts are the same, True
            if s1_count == s2_count:
                return True

        # Otherwise False
        return False
        