class Solution(object):
    def search(self, nums, target):
        nums.sort()
        low=0
        n=len(nums)
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if(nums[mid]==target):
                return True
            elif(nums[mid]>target):
                high=mid-1
            else:
                low=mid+1
        return False  
        
        