class Solution(object):
    def minEatingSpeed(self, piles, h):
        low=1
        high=max(piles)
        ans=0
        while low<=high:

            mid=(low+high)//2
            total_hour=0
            for pile in piles:
                total_hour=(pile+mid-1)//mid+total_hour
        
            if(total_hour<=h):
                ans=mid
                high=mid-1
            else:
                low=mid+1
               
        return ans
 
        """ 
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        