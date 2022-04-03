class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = [-1]
        n = len(heights)
        area = 0
        i = 0
        left_smaller = [-1]*len(heights)
        right_smaller = [n]*len(heights)
        while i < len(heights):
            while stack and (stack[-1] != -1) and (heights[stack[-1]] > heights[i]):
                right_smaller[stack[-1]] = i
                stack.pop()
            if((i > 0) and (heights[i] == heights[i-1])):
                left_smaller[i] = left_smaller[i-1]
            else:
                left_smaller[i] = stack[-1]
            stack.append(i)
            i += 1
        for j in range(0, len(heights)):
            area = max(area, heights[j]*(right_smaller[j]-left_smaller[j]-1))
        return area
        