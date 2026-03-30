class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        comb = []
        digitsToChar = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def backtrack(i):
            #base case
            if i == len(digits):
                #concatenate a list of str to a str
                res.append(''.join(comb))
                return
            
            #for each digit we iterate the potential chars 
            #and backtrack after we are done for each digit

            #each call should not iterate all the digits, just the current digit
            
            chars = digitsToChar[digits[i]]
            for char in chars:
                comb.append(char)
                backtrack(i + 1)
                comb.pop()
            
        backtrack(0)
        return res
        





