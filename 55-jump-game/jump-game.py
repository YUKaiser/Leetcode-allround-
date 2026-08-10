class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_J=0
        for i in range(len(nums)):
            max_J=max(max_J,i+nums[i])
            if max_J==len(nums)-1:
                break
            if i==max_J:
                return False
        return True