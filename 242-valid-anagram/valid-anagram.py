class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        dicta_s={}
        for i in range(len(s)):
            dicta_s[s[i]]=dicta_s.get(s[i],0)+1
        
        for cr in t:
            if cr not in dicta_s:
                return False
            else:
                if dicta_s[cr]==0:
                    return False
                else:
                    dicta_s[cr] -=1
        
        return True