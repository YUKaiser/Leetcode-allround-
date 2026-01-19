class Solution(object):
    def maxProfit(self, prices):
        maxprofit=0
        n=len(prices)
        min_cost=float('inf')
        for i in range(n):
            min_cost=min(min_cost,prices[i])
            if min_cost<=prices[i]:
                maxprofit=max(maxprofit,prices[i]-min_cost)
            
        return maxprofit
        """
        :type prices: List[int]
        :rtype: int
        """
        