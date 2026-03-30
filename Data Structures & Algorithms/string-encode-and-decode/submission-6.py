"""
Encode by int(length)#str
Decode by using two pointers
"""
class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res

            
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            #j at start of num
            while s[j] != '#':
                j += 1
            #j now at #
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])

            #update i
            i = j + 1 + length

        return res

#time: O(n) for both, space: O(n) for both
    