class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        num = ""
        while i < len(s):
            while s[i] != "#":
                num += s[i]
                i += 1
            if i == '#':
                i += 1            
            decoded.append(s[i+1:i+int(num)+1])
            i += int(num) + 1
            num = ""
        return decoded


            

