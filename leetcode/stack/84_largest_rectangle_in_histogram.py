from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        max_a = 0
        pop = stack.pop
        append = stack.append
        
        for i, h in enumerate(heights):
            while heights[stack[-1]] > h:
                area = heights[pop()] * (i - stack[-1] - 1)
                if area > max_a:
                    max_a = area
            append(i)
        heights.pop()
        return max_a