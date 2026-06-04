class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Count step (equivalent to "Counter(nums)")
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        # Sort by count (equivalent to "counter.most_commons()")
        sorted_count = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        
        return [num[0] for num in sorted_count][:k]



        