class Solution(object):
    def mySqrt(self, x):
        low=1
        high=x
        r=0
        while low<=high:
            mid=(low+high)//2
            if (mid*mid>x):
                high=mid-1
            else:
                r=mid
                low=mid+1
        return r
        """
        :type x: int
        :rtype: int
        """
        