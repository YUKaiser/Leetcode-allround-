class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        i=0
        n=len(s)
        dicta={}
        for j in range(n):
            dicta[s[j]]=dicta.get(s[j],0)+1
            while dicta.get('a',0)>0 and dicta.get('b',0)>0 and dicta.get('c',0)>0:
                count+=n-j
                dicta[s[i]]-=1
                i+=1
        return count

