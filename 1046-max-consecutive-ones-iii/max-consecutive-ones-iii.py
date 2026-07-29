class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxi=0
        i=0
        count=0
        for j in range(len(nums)):
            if nums[j]==0:
                count+=1
            while count>k:
                if nums[i]==0:
                    count-=1
                i+=1
            maxi=max(maxi,j-i+1)
        return maxi