class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            num_i = numbers[i]
            num_j = numbers[j]
            if num_i + num_j == target:
                return [i+1, j+1]
            
            if num_i + num_j < target:
                i += 1
            else:
                j -= 1
        
        