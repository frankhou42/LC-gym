class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #edge case when t is empty str
        if t == "": return ""


        window, countT = {}, {}

        #initialize countT dict
        for c in t:
            countT[c] = countT.get(c, 0) + 1
            #note: c is the key, countT.get(sth) is equal to countT[c]
            #      must use .get(c, 0) the second param is when key is not in dict and we just get 0
        #have and need to check if window is valid
        have, need = 0, len(countT) 
        
        #tip: float infinity is a huge number
        resLen, res = float("infinity"), [-1, -1]
        #keep track of minimum window and its index

        l = 0

        for r in range(len(s)):
            
            ##this segment of code is to just udpate hashmap and check the have variable char when incrementing window size

            #add the character on R ptr to the window dict, characters that is in s will have a place in window 
            if s[r] in countT:
                window[s[r]]  = window.get(s[r], 0) + 1
            
            #check when we added the character in window if its same
            #freq as countT, if so increment have
            if s[r] in countT and countT[s[r]] == window[s[r]]:
                have += 1

            ##when have == need we try to find smaller window based on the current valid window and keep
            ## moving the valid window's L ptr
            while have == need:
                #update the res infos if found smaller window size
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                #remove a char from window by shifting L ptr
                if s[l] in window:
                    window[s[l]] -= 1
                
                if s[l] in window and window[s[l]] < countT[s[l]]:
                    have -= 1
                
                l += 1
        
        #for s[l:r], r index is excluded
        return s[res[0] : res[1]  + 1] if resLen != float("infinity") else ""



                
                
            


