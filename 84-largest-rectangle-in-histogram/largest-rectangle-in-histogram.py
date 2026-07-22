class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n=len(heights)
        right_side_min=[n]*n
        right_stk=[]
        for i in range(n-1,-1,-1):
            while right_stk and heights[i]<heights[right_stk[-1]]:
                right_stk.pop()
            if right_stk:
                right_side_min[i]=right_stk[-1]
            right_stk.append(i)
        left_side_min=[-1]*n
        left_stk=[]
        for i in range(n):
            while left_stk and heights[i]<=heights[left_stk[-1]]:
                left_stk.pop()
            if left_stk:
                left_side_min[i]=left_stk[-1]
            left_stk.append(i)
        max_area = 0

        for i in range(n):
            width = right_side_min[i] - left_side_min[i] - 1
            area = heights[i] * width
            max_area = max(max_area, area)

        return max_area
