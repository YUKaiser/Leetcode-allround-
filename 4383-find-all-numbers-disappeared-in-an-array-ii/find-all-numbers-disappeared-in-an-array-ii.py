class Solution(object):
    def findDisappearedNumbers(self, nums, lower, upper):
        res = []

        nums = set(nums)

        for j in range(lower, upper + 1):
            if j in nums:
                res.append(0)
            else:
                res.append(j)

        ans = []
        temp = []

        for x in res:
            if x != 0:
                temp.append(x)
            else:
                if temp:
                    ans.append([temp[0], temp[-1]])
                    temp = []

        if temp:
            ans.append([temp[0], temp[-1]])

        return ans