class Solution(object):
    def search(self, nums, target):
        
        result=self.binarySearch(nums,nums.index(min(nums)),len(nums)-1,target)
        if(result==-1):
            result=self.binarySearch(nums,0,nums.index(min(nums))-1,target)
        return result
    def binarySearch(self,nums,low,high,target):
        while low<=high:
            mid=(low+high)//2
            if(nums[mid]==target):
                
                return mid
            elif(nums[mid]>target):
                high=mid-1
            else:
                low=mid+1
        return -1
        
  

       
     