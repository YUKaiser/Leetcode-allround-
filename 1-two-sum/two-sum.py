class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dicta={}
        for j in range(len(nums)):
            if target-nums[j] in dicta:
                return [dicta[target-nums[j]],j]
            else:
                dicta[nums[j]]=j
        return 0