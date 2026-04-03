class Solution(object):
    def isIsomorphic(self, s, t):
        dicta={}
        for i in range(len(s)):
            if s[i] in dicta:
                if dicta[s[i]]!=t[i]:
                    return False
            elif(t[i] in dicta.values()):
                if s[i] not in dicta:
                    return False
            else:
                dicta[s[i]]=t[i]
        return True
        
       
        