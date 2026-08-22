class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cnt=0
        while n>0:
            if n%2==1:
                cnt+=1
            n=n//2
        if cnt==1:
            return True
        return False