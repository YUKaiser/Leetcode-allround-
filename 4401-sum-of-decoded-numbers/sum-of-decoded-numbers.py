class Solution(object):
    def sumDecoded(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD=10**9+7
        a=nums
        ans=0
        for i in a:
            w=i%10
            d=i//10
            s=str(d)
            x=int(s[:w])
            y=int(s[w:])
            ans+=self.FindPow(x,y,MOD)
            ans%=MOD
        
            
        return ans
    def FindPow(self, a, b,MOD):
        if b==0:
            return 1
        half=self.FindPow(a,b//2,MOD)
        res=(half*half)%MOD
        if b%2==1:
            res=(a*res)%MOD
        return res