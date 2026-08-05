class Solution(object):
    def countKConstraintSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        cnt=0
        for i in range(len(s)):
            dicta={'0':0,'1':0}
            for j in range(i,len(s)):
                dicta[s[j]]=dicta.get(s[j])+1
                if dicta['0']>k and dicta['1']>k:
                    break
                cnt+=1
        return cnt
        
        