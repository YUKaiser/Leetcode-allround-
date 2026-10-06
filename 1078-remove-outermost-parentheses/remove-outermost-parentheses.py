class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt=0
        res=""
        for i in range(len(s)):
            if s[i]=="(":
                cnt+=1
                if cnt>1:
                    res+=s[i]
            else:
                cnt-=1
                if cnt>0:
                    res+=s[i]
        return res