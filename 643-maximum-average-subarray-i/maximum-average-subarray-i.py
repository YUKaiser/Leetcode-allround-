class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sumi=sum(nums[:k])
        maxi=sumi
        
        i=0
        for j in range(k,len(nums)):
            sumi+=nums[j]-nums[i]
            i+=1
            maxi=max(sumi,maxi)
        return maxi/k