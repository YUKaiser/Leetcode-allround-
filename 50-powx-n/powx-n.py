class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        if n<0:
            x=1/x
            n=-n
        half=self.myPow(x,n//2)
        res=half*half
        if n%2==1:
            res=x*res
        return res