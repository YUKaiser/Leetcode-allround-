class Solution(object):
    def rearrangeArray(self, nums):
        arr_final=[0]*len(nums)
        i=0
        j=1
        for num in nums:
            if num >0:
                arr_final[i]=num
                i=i+2
            else:
                arr_final[j]=num
                j=j+2
        return arr_final
    
        