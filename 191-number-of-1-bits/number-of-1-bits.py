class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res=[]
        while n>0:
            if n%2==1:
                res.append(1)
            else:
                res.append(0)
            n=n//2
        res.reverse()
        return res.count(1)