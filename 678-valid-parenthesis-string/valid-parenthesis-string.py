class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s[0]==')':
            return False
        left_stk=[]
        star_stk=[]
        for i in range(len(s)):
            if s[i]==")":
                if len(left_stk)!=0:
                    left_stk.pop()
                elif len(star_stk)!=0:
                    star_stk.pop()
                else:
                    return False
            elif s[i]=="*":
                star_stk.append(i)
            else:
                left_stk.append(i)
        while left_stk and star_stk:
            if left_stk[-1]>star_stk[-1]:
                return False

            star_stk.pop()
            left_stk.pop()
        if len(left_stk)!=0:
            return False
        return True