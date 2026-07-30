class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ans = 0

        for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            i = 0
            diff = 0

            for j in range(len(s)):
                if s[j] != ch:
                    diff += 1

                while diff > k:
                    if s[i] != ch:
                        diff -= 1
                    i += 1

                ans = max(ans, j - i + 1)

        return ans  