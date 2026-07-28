class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        length=float('-inf')
        dicta={}
        if not s:
            return 0
        for j in range(len(s)):
            if s[j] in dicta and dicta[s[j]]>=i:
                i=dicta[s[j]]+1
                 
            dicta[s[j]]=j
            length=max(j-i+1,length)
        return length