class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        # Iterate through each bar in the histogram
        for i, h in enumerate(heights):
            # 'start' tracks how far left the current bar can extend
            start = i
            # While the stack isn’t empty and the last bar is taller than the current one,
            # pop it and compute its maximal rectangle area ending at index i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # Width is (current index − start index of that bar)
                area = height * (i - index)
                maxArea = max(maxArea, area)
                # Update start so the new bar can extend as far left as the popped bar
                start = index

            # Push the current bar with its adjusted left boundary
            stack.append([start, h])

        # Any remaining bars in the stack can extend to the end of the histogram
        for index, height in stack:
            area = height * (len(heights) - index)
            maxArea = max(maxArea, area)

        return maxArea
