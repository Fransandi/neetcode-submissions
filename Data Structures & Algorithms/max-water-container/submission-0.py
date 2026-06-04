class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j, max_water = 0, len(heights) - 1, 0
        while i < j:
            bar_1 = heights[i]
            bar_2 = heights[j]
            water = min(bar_1, bar_2) * (j-i)
            max_water = max(max_water, water)

            if bar_1 < bar_2:
                i += 1
            else:
                j -= 1

        return max_water
        