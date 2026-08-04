class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)

        if k == n:
            return sum(cardPoints)

        left_pre = [0] * (k + 1)
        right_pre = [0] * (k + 1)

        left_sum = 0
        right_sum = 0

        for i in range(1, k + 1):
            left_sum += cardPoints[i - 1]
            left_pre[i] = left_sum

        for i in range(1, k + 1):
            right_sum += cardPoints[n - i]
            right_pre[i] = right_sum

        sumi = 0

        for i in range(k + 1):
            sumi = max(sumi, left_pre[i] + right_pre[k - i])

        return sumi