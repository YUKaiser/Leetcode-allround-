class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxi=max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies>=maxi:
                candies[i]=True
            else:
                candies[i]=False
        return candies

        