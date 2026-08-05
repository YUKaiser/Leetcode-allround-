class Solution(object):
    def countKConstraintSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        cnt=0
        i=0
        dicta={'1':0,'0':0}
        for j in range(len(s)):
            dicta[s[j]]=dicta.get(s[j])+1
            while dicta['0']>k and dicta['1']>k:
                dicta[s[i]]-=1
                i+=1
            cnt+=j-i+1
        return cnt

        