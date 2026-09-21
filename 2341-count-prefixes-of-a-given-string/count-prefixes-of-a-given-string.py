class Solution(object):
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        res=[]
        cnt=0
        for i in range(len(s)):
            
            cnt+=words.count(s[:i+1])
        return cnt