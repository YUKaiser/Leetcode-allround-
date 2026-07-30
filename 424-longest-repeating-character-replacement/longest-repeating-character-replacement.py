class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_fre=0
        res_max=0
        i=0
        dicta={}
        for j in range(len(s)):
            dicta[s[j]]=dicta.get(s[j],0)+1
            max_fre=max(dicta[s[j]],max_fre)
            while (j-i+1)-max_fre >k:
                dicta[s[i]]=dicta.get(s[i])-1
                max_fre=max(max_fre,dicta[s[i]])
                i+=1
            res_max=max(j-i+1,res_max)
        return res_max