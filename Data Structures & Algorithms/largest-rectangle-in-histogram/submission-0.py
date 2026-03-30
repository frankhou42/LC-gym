class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        #go through each bar while the next bar is not in incrementing order
        #we would then pop out recent bars that are greater than the next bar
        #and calcualte and update the max area of each incrementing recent bar 
        #until we find a bar that is smaller than or equal to the next bar.

        #after we have one passed the array of heights we would loop through the 
        #remaining bars in the stack and calculate the max area from its index to the end of
        #arr (since its left behind because the bars after it is smaller than or equal to its height
        #since other wise it would have been poped because its larger than all the bars after it)

        for i, h in enumerate(heights):
            #consider case where the height we add is not larger than the height before it
            #pop all that is before that is larger than the height we add so that we can find the most beginning index that 
            #we can make a rectangle
            start = i #in case where we don't pop the stack, incrementing order
            #start ensures we get the full possible width of rectangle e.g. [5,6,2] start index for 2 is 0
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                #we pop cause we know exactly how wide that ractangle can be (the start is start and the end will be the curr index as the next rectangle is smaller)
                area = height * (i - index)
                maxArea = max(area, maxArea)
                start = index

            stack.append([start, h])
            #add new heights with correct start so we know how left it cna go

        #leftover bars are bars that are smaller than all the bars after it, meaning it can extend all the way to the right
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
            

        return maxArea


            
