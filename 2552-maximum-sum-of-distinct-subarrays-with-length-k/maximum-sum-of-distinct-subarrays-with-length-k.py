class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sumi=0
        maxi=0
        duplicate=0
        dicta={}
        for i in range(k):
            sumi+=nums[i]
            if nums[i] not in dicta:
                dicta[nums[i]]=1
            else:
                if dicta[nums[i]]==1:
                    duplicate+=1
                dicta[nums[i]]+=1
        if duplicate==0:
            maxi=max(sumi,maxi)
        i=0
        j=k-1
        while j<len(nums)-1:
            sumi-=nums[i]
            dicta[nums[i]]=dicta.get(nums[i])-1
            if dicta[nums[i]]==1:
                duplicate-=1
            i+=1
            j+=1
            sumi+=nums[j]
            if nums[j] not in dicta or dicta[nums[j]]==0:
                dicta[nums[j]]=1
                
            else:
                if dicta[nums[j]]==1:
                    duplicate +=1
                dicta[nums[j]]+=1

            if duplicate==0:
                maxi=max(sumi,maxi)
        return maxi