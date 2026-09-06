class Solution(object):
    def countGoodRotations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num1=nums+nums
        a=0
        b=len(nums)//2-1
        left=sum(num1[a:b+1])
        c=len(nums)//2
        d=len(nums)
        right=sum(num1[c:d])
        
        cnt=0
        while d<len(num1):
            if left>right:
                cnt+=1
            left-=num1[a]
            a+=1
            b+=1
            left+=num1[b]
            right-=num1[c]
            c+=1
            d+=1
            right+=num1[d-1]
        return cnt