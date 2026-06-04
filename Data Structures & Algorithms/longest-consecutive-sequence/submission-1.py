class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        candidates = [n for n in nums if n-1 not in nums]

        solution = 0
        for candidate in candidates:
            current = 0
            while candidate in nums:
                current += 1
                candidate += 1
            solution = max(solution, current)
        
        return solution

        