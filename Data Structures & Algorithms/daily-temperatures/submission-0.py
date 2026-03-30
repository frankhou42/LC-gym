class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []#store [temp, index]
        res = [0] * len(temperatures)

        # Syntax: for x, y (x is index and y is val) 
        for i, temp in enumerate(temperatures):
            #pop elements out of stack if stack is not empty
            #and prev element's temp is small than the temp 
            #we are going to add
            while stack and stack[-1][0] < temp:
                #with each pop, we find the corresponding temperature day index
                #with stack and update res by using i - tempInx
                tempInd = stack.pop()[1]
                res[tempInd] = i - tempInd

            #after poping and updating res we can now add 
            stack.append([temp, i])
        return res


            
            
            