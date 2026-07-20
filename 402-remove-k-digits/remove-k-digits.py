class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num)==k:
            return "0"
        stk=[]
        
        for i in range(len(num)):
            while stk and k>0 and num[i]<stk[-1]:
                stk.pop()
                k-=1

            stk.append(num[i])
        
        while k>0:
            stk.pop()
            k-=1
        a="".join(stk)

        if int(a)==0:
            return "0"
        else:
            return a.lstrip("0")