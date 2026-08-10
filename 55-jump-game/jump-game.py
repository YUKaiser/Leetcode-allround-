class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) == 1:
            return True

        store = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= store:
                store = i

        return store == 0