class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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

        def backtrack(start):
            #base case
            if len(comb) == len(digits):
                #concatenate a list of str to a str
                res.append(''.join(comb))
                return
            
            #for each digit we iterate the potential chars 
            #and backtrack after we are done for each digit
            for i in range(start, len(digits)):
                chars = digitsToChar[digits[i]]
                for char in chars:
                    comb.append(char)
                    backtrack(i + 1)
                    comb.pop()
        if digits:
            backtrack(0)
            return res
        else:
            return []




