class Solution(object):
    def frequencySort(self, s):
        dicta_s={}
        result=""
        
        for i in range(len(s)):
            dicta_s[s[i]]=dicta_s.get(s[i],0)+1
        
        for key in sorted(dicta_s,key=dicta_s.get,reverse=True):
            result +=key*dicta_s[key]
        return result