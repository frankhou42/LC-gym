class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0

        res = 0
        
        count = {}

        for r in range(len(s)):
            #build char-freq hashmap to find most frequent character in the window
            #in each window we check if the window is valid, 
            #if so we increment r ptr and keep going through all possible optimal windows
            #or else we increase l ptr till its valid
            count[s[r]] = count.get(s[r], 0) + 1

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l+=1
                #decrement needed as we still want to keep track of curr window
            res = max(res, r - l + 1)

        return res
            