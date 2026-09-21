import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        if len(piles)==h:
            return max(piles)
        low=1
        high=max(piles)
        mini=float('inf')
        while low<=high:
            mid=(low+high)//2
            if self.calculatespeed(piles,h,mid) <=h:
                mini=min(mini,mid)
                high=mid-1
            else:
                low=mid+1
        return mini
    def calculatespeed(self,piles,h,mid):
        t_h=0
        for pile in piles:
            t_h+=math.ceil(float(pile)/mid)
        return t_h
        