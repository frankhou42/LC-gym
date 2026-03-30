class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0

        res = 0
        
        count = {}

        maxf = 0

        for r in range(len(s)):
            #build char-freq hashmap to find most frequent character in the window
            #in each window we check if the window is valid, 
            #if so we increment r ptr and keep going through all possible optimal windows
            #or else we increase l ptr till its valid
            count[s[r]] = count.get(s[r], 0) + 1
            #only record maxf since smaller window can't improve answer
            #this allows us to not need to traverse count hashmap to find max count
            #allowing solution to be O(1) just compare with maxf and added char with
            #R ptr
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l+=1
                #decrement needed as we still want to keep track of curr window
            res = max(res, r - l + 1)

        return res
            