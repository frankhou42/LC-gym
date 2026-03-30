"""
create a big hashmap where the key is 26 letters freq and the 
value is the list of anagrams that matches the key.
Iterate through values of hashmap and append to list create final
output
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord("a")] += 1
            hashmap[tuple(key)].append(s)
        
        res = []
        for _, val in hashmap.items():
            res.append(val)

        return res

#CAUTION: Since hashmap keys are immutable, keys can't be list, must be tuple