class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        for j in range(n+1):
            if (j not in nums):
                return j
        
            
