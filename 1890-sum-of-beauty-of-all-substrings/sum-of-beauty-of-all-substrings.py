class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt=0
        
        for i in range(len(s)):
            dicta={}
            maxi=float("-inf")
            mini=float("inf")
            for j in range(i,len(s)):
                dicta[s[j]]=dicta.get(s[j],0)+1
                maxi=max(maxi,dicta[s[j]])
                if len(dicta)>1:
                    mini=min(dicta.values())
                    cnt+=maxi-mini
        return cnt
        