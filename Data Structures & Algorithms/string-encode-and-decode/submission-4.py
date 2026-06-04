class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for s in strs:
            code += str(len(s)) + "." + s
        return code


    def decode(self, s: str) -> List[str]:
        solution = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '.':
                j += 1

                if j >= len(s):
                    break
            
            length = int(s[i:j])
            print(length)

            solution.append(s[j+1:j+1+length])
            print(solution)

            i = j+1+length
          

        return solution
