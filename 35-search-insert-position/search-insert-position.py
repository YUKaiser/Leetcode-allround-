class Solution(object):
    def searchInsert(self, nums, target):
        n=len(nums)
        low=0
        high=(n-1)
        
        while (low<=high):
            mid=(low+high)//2
            for i in range(n):
                if(nums[i]==target):
                    return i
                    break
            
            if(nums[mid]-target==1):
                return mid
            elif((nums[mid]-target)==-1):
                return mid+1
            

            elif(nums[mid]<target):
                low=mid+1
            else:
                high=mid-1
        if target<nums[0]:
            return 0
        else:
            return n
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        