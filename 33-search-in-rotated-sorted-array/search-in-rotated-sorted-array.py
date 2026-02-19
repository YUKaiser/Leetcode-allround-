class Solution(object):
    def search(self, nums, target):
        # Find the pivot (index of the minimum element)
        pivot = nums.index(min(nums))
        
        # Search the right side of the pivot
        result = self.binarySearch(nums, target, pivot, len(nums) - 1)
        
        # If not found, search the left side
        if result == -1:
            result = self.binarySearch(nums, target, 0, pivot - 1)
            
        return result

    # Pass nums and target as arguments so the function can see them
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
