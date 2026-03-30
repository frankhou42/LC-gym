class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            sortedS = ''.join(sorted(s)) #sorted string
            
            # put actual string in same dict record if the sorted str is same, else make a new record
            # the dict would eventually be filled up with outer loop
            if sortedS in res:
                res[sortedS].append(s)
            else:
                res[sortedS] = [s]

        #output list of all the values in dict (any order allowed)
        return list(res.values())