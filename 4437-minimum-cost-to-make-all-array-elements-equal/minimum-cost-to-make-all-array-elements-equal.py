class Solution(object):
    def minCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_cost = float("inf")
        for i in range(1, len(nums) - 1):
            # CORRECTION: Skip if 'i' is part of the same block already handled by 'i - 1' -> makes it O(n)!
            if i > 1 and nums[i] == nums[i - 1]:
                continue

            left = i - 1
            left_cost = 0
            while left >= 0:
                if nums[left] != nums[i]:
                    left_cost = nums[i] * (i)
                    break
                left -= 1

            right = i + 1
            right_cost = 0
            while right <= len(nums) - 1:
                i = right - 1
                if nums[right] != nums[i]:
                    right_cost = (len(nums) - i - 1) * nums[i]
                    break
                right += 1

            cost = left_cost + right_cost
            total_cost = min(cost, total_cost)
        return total_cost