class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cnt_left=0
        cnt_right=0
        for i in range(len(s)):
            if s[i]=='(' or s[i]=="*":
                cnt_left+=1
            else:
                cnt_left-=1
                if cnt_left<0:
                    return False
        for i in range(len(s)-1,-1,-1):
            if s[i]==')' or s[i]=="*":
                cnt_right+=1
            else:
                cnt_right-=1
                if cnt_right<0:
                    return False
        return True    