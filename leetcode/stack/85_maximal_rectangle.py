from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        max_area = 0
        def largestRectangleArea(heights):
            stack = []
            max_a = 0
            for i, h in enumerate(heights + [0]):
                while stack and heights[stack[-1]] > h:
                    mid = stack.pop()
                    bar_height = heights[mid]
                    left_b = stack[-1] if stack else -1
                    width = i - left_b - 1
                    max_a = max(max_a, bar_height * width)
                stack.append(i)
            return max_a

        for r in matrix:
            for c in range(n):
                if r[c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0
            max_area = max(max_area, largestRectangleArea(heights))
        return max_area