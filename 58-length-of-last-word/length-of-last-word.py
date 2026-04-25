class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=s.split()
        length=len(a[len(a)-1])
        return length