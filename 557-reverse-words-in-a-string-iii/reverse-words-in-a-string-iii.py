class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lis=s.split(" ")
        
        for i in range(len(lis)):
            lis[i]=lis[i][::-1]
        a=" ".join(lis)
        return a
