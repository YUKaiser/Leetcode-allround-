class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        s=set(nums)
        maxi=0
        for num in s:
            if nums.count(num)>maxi:
                maxi=nums.count(num)
                a=num
        return a