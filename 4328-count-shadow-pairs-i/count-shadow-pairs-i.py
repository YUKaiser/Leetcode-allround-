class Solution(object):
    def shadowPairs(self, nums):
        cnt = 0
        stk = []

        for i in range(len(nums)):

            while stk and nums[i] < stk[-1]:
                stk.pop()

            # find how many elements in stk are < nums[i]
            l = 0
            r = len(stk)

            while l < r:
                mid = (l + r) // 2

                if stk[mid] < nums[i]:
                    l = mid + 1
                else:
                    r = mid

            cnt += l

            stk.append(nums[i])

        return cnt