from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        sorted_count = counter.most_common()
        return [num[0] for num in sorted_count][:k]

        