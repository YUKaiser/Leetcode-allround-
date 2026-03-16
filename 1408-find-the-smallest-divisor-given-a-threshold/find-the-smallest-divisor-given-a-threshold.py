class Solution(object):
    def smallestDivisor(self, nums, threshold): 
        l,h=1,max(nums)
        while l<=h:
            mid=(l+h)//2
            if sum(math.ceil(float(x)/mid) for x in nums)>threshold:
                l=mid+1
            else:
                h=mid-1
        return l
       
        # see here we write float becausw it is py2 version


        
        