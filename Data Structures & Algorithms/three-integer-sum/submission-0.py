class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen, solution = set(), []

        # Find all combinations of two numbers adding up to the target
        for n in nums:
            if target - n in seen:
                solution.append([n, target - n])
            seen.add(n)
        
        return solution
            

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []

        # Iterate through all numbers
        for i, n in enumerate(nums):

            # Get suitable pairs to create a triplet
            pairs = self.twoSum(nums[:i] + nums[i+1:], n * -1)

            # Find suitable triplets
            for pair in pairs:
                triplet = sorted([pair[0], pair[1], n])
                
                # Add triplet to the solution, if no repeated
                if triplet not in solution:
                    solution.append(triplet)

        return solution

        