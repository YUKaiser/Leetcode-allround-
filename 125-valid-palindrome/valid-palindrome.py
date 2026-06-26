class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a="".join(ch.lower() for ch in s if ch.isalnum())
        if a==a[::-1]:
            return True
        return False