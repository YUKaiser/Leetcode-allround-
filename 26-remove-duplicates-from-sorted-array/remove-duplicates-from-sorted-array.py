class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=[]
        dicta={}
        for i in range(len(nums)):
            dicta[nums[i]]=dicta.get(nums[i],0)+1
            if dicta[nums[i]]==1:
                a.append(nums[i])
        j=0
        for i in range(len(a)):
            nums[i]=a[i]
            j+=1
        while j<len(nums):
            nums[j]="_"
            j+=1
        return len(a)
    
                

        