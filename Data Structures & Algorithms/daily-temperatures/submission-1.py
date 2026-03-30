class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            #the stack should be in descending order 
            #since we are waiting for a temp thats larger
            #than the first temp
            #with each pop we update the distance of temp in stack's day index
            #in res using day index difference of newly inserted temp and temp in stack

            #when there is smaller temp than the one being inserted in stack
            #if larger or equal it stays
            while stack and stack[-1][0] < temp :
                dayIndex = stack.pop()[1]
                res[dayIndex] = index - dayIndex
            
            stack.append([temp, index])
        
        return res
