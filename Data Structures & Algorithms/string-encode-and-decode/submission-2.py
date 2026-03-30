class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += "#"
            res += s
        
        return res

        
    def decode(self, s: str) -> List[str]:
 #4#neet#4code#4love#3you
        #use 2 ptrs
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1

            #j ptr on #
            length = int(s[i:j])

            i = j + 1
            j = i + length

            res.append(s[i:j])

            i = j
        
        return res
                
