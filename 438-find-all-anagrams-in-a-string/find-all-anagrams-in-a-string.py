class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p)>len(s):
            return []
        dicta1={}
        dicta2={}
        for i in range(len(p)):
            dicta1[p[i]]=dicta1.get(p[i],0)+1
        for j in range(len(p)):
            dicta2[s[j]]=dicta2.get(s[j],0)+1
        left=0
        right=len(p)-1
        res=[]
        while right <=len(s)-1:
            if dicta1==dicta2:
                res.append(left)
        
            dicta2[s[left]]-=1
            if dicta2[s[left]]==0:
                del dicta2[s[left]]
            left+=1
            right+=1
            if right<len(s):
                dicta2[s[right]]=dicta2.get(s[right],0)+1
        return res

