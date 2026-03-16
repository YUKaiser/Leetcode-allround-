class Solution(object):
    def smallestDivisor(self, nums, threshold): 
        low=1
        high=max(nums)
        result=high
        while low<=high:
            mid=(low+high)//2
            a=self.sum_a(nums,mid)
            if a<=threshold:
                result=mid
                high=mid-1
            else:
                low=mid+1
        return result
    def sum_a(self,nums,mid):
         return sum(math.ceil(float(x )/ mid) for x in nums)
        


        
        