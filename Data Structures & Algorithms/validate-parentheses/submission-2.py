class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = { ')' : '(', 
                    ']' : '[',
                    '}' : '{'}
        
        stack = []
                    

        for c in s:
            if c in hashmap.values():
                stack.append(c)
            
            #pop when stack has stuff inside
            elif c in hashmap and stack and stack[-1] == hashmap[c]:
                stack.pop()

            else:
                return False
        
        return False if stack else True

        

