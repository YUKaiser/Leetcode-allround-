class Solution(object):
    def isIsomorphic(self, s, t):
        dicta_s_to_t={}
        dicta_t_to_s={}
        for i in range(len(s)):
            if s[i] in dicta_s_to_t:
                if dicta_s_to_t[s[i]]!=t[i]:
                    return False
            else:
                dicta_s_to_t[s[i]]=t[i]
            
            if t[i] in dicta_t_to_s:
                if dicta_t_to_s[t[i]]!=s[i]:
                    return False
            else:
                dicta_t_to_s[t[i]]=s[i]
        return True
        
       
        