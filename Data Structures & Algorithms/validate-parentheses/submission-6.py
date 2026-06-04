class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(': ')', '[': ']', '{': '}'}

        for char in s:
            if char in brackets.keys():
                stack.append(char)
            elif stack and brackets[stack[-1]] == char:
                stack.pop()
            else:
                return False
        
        return not len(stack)




                    

        