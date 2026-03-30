class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        hashset = set()
        l = 0
        for c in s:
            #remove all chars b4 and including the repeating char
            #and add the char at the end as it is in the new sequence
            #at last update the max_length 
            while c in hashset:
                hashset.remove(s[l])
                l+=1
            hashset.add(c)
            max_length = max(max_length, len(hashset))

        return max_length

            