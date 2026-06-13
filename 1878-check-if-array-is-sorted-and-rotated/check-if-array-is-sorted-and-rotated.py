class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a=nums+nums
        b=sorted(nums)
        for i in range(len(nums)):
            if a[i:i+len(nums)]==b:

                return True
        return False
        