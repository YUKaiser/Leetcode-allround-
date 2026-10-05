class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dicta={}
        for i in range(len(s)):
            dicta[s[i]]=dicta.get(s[i],0)+1

        for j in range(len(s)):
            if dicta[s[j]]==1:
                return j
        return -1