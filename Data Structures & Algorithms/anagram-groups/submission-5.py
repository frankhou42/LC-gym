class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        hashmap = defaultdict(list) #default values are lsits
        #use frequency table as key and value is the array of anagrams
        for s in strs:
            arr = [0] * 26
            for c in s:
                arr[ord(c) - ord('a')] += 1
            #hashmap must have tuple as keys not list
            hashmap[tuple(arr)].append(s)
            
        for v in hashmap.values():
            res.append(v)
        
        return res