class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedPairs = [[p,s] for p, s in zip(position, speed)] #New Syntax: zip command
        sortedPairs.sort(reverse=True)#New Syntax: reverse True command
        #sort is based on the first element in the sub-arr

        #start from the car closest to tgt since the closer ones
        #determines whether the car behind will be apart of the fleet
        
        stack = []

        for p, s in sortedPairs:
            #if the newly added car intersect with prev car we pop it out else remain in
            currTime = (target - p)/s
            #first append a car so that we can start the fleet
            stack.append(currTime)
            if len(stack) >= 2 and stack[-2] >= stack[-1]: #same speed same car fleet hence stack[-2] <= stack[-1]
                stack.pop()
        return len(stack)
                

    #General Rule For Stack Qs:
    #In all cases, you’re remembering past elements that haven't been solved
    #and youcompare or resolve against the most recent added item. (top of stack)
    #That’s why a stack—pushing and popping at the end—is perfect.