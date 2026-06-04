class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Count the number of zeroes
        zeros = sum([1 for n in nums if n == 0])

        # Edge case: If more than 1 zero, return an array full of zeros
        if zeros >= 2:
            return [0] * len(nums)

        # Get the total product of all numbers
        total_prod = 1
        for n in nums:
            if n: total_prod *= n

        solution = []

        # Edge case: there's a zero
        if zeros == 1:
            for n in nums:
                solution.append(0 if n else total_prod)
        
        # Calculate the solution
        else:
            for n in nums:
                solution.append(int(total_prod / n))
        
        return solution


        
        


        
        
        