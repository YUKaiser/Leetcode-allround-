class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sumi=0
        maxi=float('-inf')
        for j in range(k):
            sumi+=nums[j]
        maxi=max(maxi,sumi/k)
        i=0
        j=k-1
        while j<len(nums)-1:
            sumi-=nums[i]
            i+=1
            j+=1
            sumi+=nums[j]
            maxi=max(sumi/k,maxi)
        return maxi