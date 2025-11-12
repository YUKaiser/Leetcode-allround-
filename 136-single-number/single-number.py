class Solution(object):
    def singleNumber(self, nums):
        count=1
        n=len(nums)
        for num in nums:
            if nums.count(num)==count:
                return num