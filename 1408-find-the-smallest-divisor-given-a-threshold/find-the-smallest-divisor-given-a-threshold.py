class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        if len(nums)==threshold:
            return max(nums)
        low=1
        high=max(nums)
        mini=float('inf')
        while low<=high:
            mid=(low+high)//2
            a=self.sumNums(nums,mid)
            if a <=threshold:
                mini=min(mid,mini)
                high=mid-1
            else:
                low=mid+1
        return mini
    def sumNums(self,nums,mid):
        res=0
        for num in nums:
            res+=math.ceil(num/mid)
        return res
        