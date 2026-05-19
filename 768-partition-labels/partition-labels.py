class Solution(object):
    def partitionLabels(self, s):

        dicta={}
        for i in range(len(s)-1,-1,-1):
            if s[i] not in dicta:
                dicta[s[i]]=i
        curr_len=0
        right=0
        lis=[]
        for i in range(len(s)):
            right=max(right,dicta[s[i]])
            curr_len +=1
            if i==right:
                lis.append(curr_len)
                curr_len=0
        return lis



        
    
        