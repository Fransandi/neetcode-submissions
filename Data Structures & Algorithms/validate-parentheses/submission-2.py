class Solution:
    def isValid(self, s: str) -> bool:

        brackets = {
            '(': ')',
            '[': ']',
            '{': '}',
        }

        stack = []

        for c in s:
            if c in brackets.keys():
                stack.append(c)
            else:

                if not len(stack):
                    return False

                if brackets[stack.pop()] != c:
                    return False
        
        return len(stack) == 0

                    

        