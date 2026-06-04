class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()
        
        for i, n in enumerate(nums):
            diff = target - n

            if diff in dic:
                return [dic[diff], i]
            dic[n] = i

            

        
        