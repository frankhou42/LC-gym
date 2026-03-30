class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }

        stack = []
        for c in s:
            if c not in hashmap:
                stack.append(c)
            elif stack and stack[-1] == hashmap[c]:
                stack.pop()
            else:
                return False
        
        return not stack
