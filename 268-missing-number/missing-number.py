class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        nums_set=set(nums)
        for j in range(n+1):
            if (j not in nums_set):
                return j
        
            
