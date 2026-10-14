class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        dicta={}
        for i in range(len(s)-1,-1,-1):
            if s[i] not in dicta:
                dicta[s[i]]=i
            else:
                continue
        i=0
        end=dicta[s[0]]
        res=[]
        for j in range(len(s)):
            if j==end:
                res.append(j-i+1)
                i=j+1
                if i <len(s):
                    end=dicta[s[i]]
            if dicta[s[j]]>end:
                end=dicta[s[j]]
        return res    