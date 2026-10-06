class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxi=0
        cnt=0
        for cr in s:
            if cr=="(":
                cnt+=1
            if cr==")":
                cnt-=1
            maxi=max(cnt,maxi)
        return maxi