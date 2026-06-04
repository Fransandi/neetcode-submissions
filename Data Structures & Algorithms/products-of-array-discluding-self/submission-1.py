class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Count the number of zeros and the total product of all numbers
        zeros, total_prod = 0, 1
        for n in nums:
            if n:
                total_prod *= n
            else:
                zeros += 1

        solution = []
        
        # Edge case: If more than 1 zero, return an array full of zeros
        if zeros > 1:
            return [0] * len(nums)
        
        # Calculate the product for each number by using a division
        for n in nums:
            if zeros:
                solution.append(0 if n else total_prod)
            else:
                solution.append(total_prod // n)

        return solution


        
        


        
        
        