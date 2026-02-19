class Solution(object):
    def search(self, nums, target):
        
        pivot = nums.index(min(nums))
        
        
        result = self.binarySearch(nums, target, pivot, len(nums) - 1)
        
        
        if result == -1:
            result = self.binarySearch(nums, target, 0, pivot - 1)
            
        return result

    
    def binarySearch(self, nums, target, low, high):
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1
