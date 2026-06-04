class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        candidates = [n for n in nums if n-1 not in nums]

        solution = 0
        for candidate in candidates:
            current = 0
            while candidate in seen:
                current += 1
                candidate += 1
            solution = max(solution, current)
        
        return solution

        