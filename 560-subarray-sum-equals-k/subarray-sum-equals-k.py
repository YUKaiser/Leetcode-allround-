class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dicta={}
        pref_sum=[]
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            pref_sum.append(s)
        cnt=0
        for j in range(len(pref_sum)):
            if pref_sum[j]-k in dicta:
                cnt+=dicta.get(pref_sum[j]-k)
            if pref_sum[j]==k:
                cnt+=1
            dicta[pref_sum[j]]=dicta.get(pref_sum[j],0)+1
        return cnt