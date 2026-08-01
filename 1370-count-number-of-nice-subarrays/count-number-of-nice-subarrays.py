class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt=0
        dicta={}
        dicta[0]=1
        res=0
        for i in range(len(nums)):
            if nums[i]%2!=0:
                cnt+=1
            
            if cnt-k in dicta:
                res+=dicta.get(cnt-k)
            dicta[cnt]=dicta.get(cnt,0)+1
        return res
      