class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        record=set()
        length=float('-inf')
        dicta={}
        if not s:
            return 0
        for j in range(len(s)):
            if s[j] in s[i:j]:
                i=dicta[s[j]]+1
                 
            dicta[s[j]]=j
            length=max(j-i+1,length)
        return length