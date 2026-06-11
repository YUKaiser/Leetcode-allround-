class Solution(object):
    def maxProfit(self, prices):
        result=0
        mi_n=float('inf')
        for i in range(len(prices)):
            mi_n=min(mi_n,prices[i])
            if mi_n<=prices[i]:
                result=max(prices[i]-mi_n,result)
        return result
        