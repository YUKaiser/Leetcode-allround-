class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_J=0
        for i in range(len(nums)):
            if i>max_J:
                return False
            max_J=max(max_J,i+nums[i])
        return True