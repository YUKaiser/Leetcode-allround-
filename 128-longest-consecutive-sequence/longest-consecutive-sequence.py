class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        a=sorted(set(nums))
        maxi=1
        cnt=1
        for i in range(len(a)-1):
            if a[i+1]-a[i]==1:
                cnt+=1
                maxi=max(cnt,maxi)
            else:
                cnt=1
            
        return maxi