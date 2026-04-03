class Solution(object):
    def longestConsecutive(self, nums):
        a = sorted(set(nums))
        
        if not a:
            return 0
        
        max_count = 1
        current = 1
        
        for i in range(len(a) - 1):
            if a[i+1] - a[i] == 1:
                current += 1
                max_count = max(max_count, current)
            else:
                current = 1
        
        return max_count
       
        