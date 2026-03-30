class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0;

        # 4#neet4#code
        while i < len(s):
            #iterate to get int length of str
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j]) #[:this is excluded], excluded the #

            i = j + 1 #update first ptr to the start of str
            j = i + length #update second ptr to int section of nxt str

            res.append(s[i:j])

            i = j
        
        return res
        
