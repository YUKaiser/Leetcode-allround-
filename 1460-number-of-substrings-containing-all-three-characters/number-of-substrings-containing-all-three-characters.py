class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        i=0
        n=len(s)
        dicta={'a':0,'b':0,'c':0}
        for j in range(n):
            dicta[s[j]]=dicta.get(s[j],0)+1
            while dicta['a']>0 and dicta['b']>0 and dicta['c']>0:
                count+=n-j
                dicta[s[i]]-=1
                i+=1
        return count

