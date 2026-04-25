class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len=0
        for i in range(0,len(s)):
            dicta={}
            for j in range(i,len(s)):
                if s[j] not in dicta:
                    dicta[s[j]]=dicta.get(s[j],1)
                    max_len=max(max_len,j-i+1)
                else:
                    break
        return max_len
        