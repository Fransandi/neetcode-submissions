class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()
        for i in range(len(nums)):
            n = nums[i]
            dic[target - n] = i
        
        for i in range(len(nums)):
            n = nums[i]
            if n in dic and dic[n] != i:
                return sorted([i, dic[n]])

        
        