class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=0
        jump=0
        while right<len(nums)-1:
            far_distance=0
            for i in range(left,right+1):
                far_distance=max(i+nums[i],far_distance)
            left=right+1
            right=far_distance
            jump+=1
        return jump