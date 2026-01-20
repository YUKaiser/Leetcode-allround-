class Solution(object):
    def rearrangeArray(self, nums):
        arr_pos=[0]*(len(nums)/2)
        arr_neg=[0]*(len(nums)/2)
        i=0
        j=0
        for num in nums:
            if num <0:
                arr_neg[i]=num
                i=i+1
            else:
                arr_pos[j]=num
                j=j+1
        k=0
        l=0
        for i in range(len(nums)):
            if((i%2)==0):
                nums[i]=arr_pos[k]
                k=k+1
            else:
                nums[i]=arr_neg[l]
                l=l+1
        return nums
            
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        