class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_side_maxi=[0]*len(height)
        right_side_maxi=[0]*len(height)
        l_maxi=float('-inf')
        for i in range(len(height)):
            l_maxi=max(height[i],l_maxi)
            left_side_maxi[i]=l_maxi
        r_maxi=float('-inf')
        for i in range(len(height)-1,-1,-1):
            r_maxi=max(height[i],r_maxi)
            right_side_maxi[i]=r_maxi
        result=0
        for i in range(len(height)):
            result+=min(left_side_maxi[i],right_side_maxi[i])-height[i]
        return result
