class Solution(object):
    def reverseWords(self, s):
        new_str=""
        a=s.split()
        for i in range(len(a)-1,-1,-1):
            new_str +=a[i]+" "
        return new_str.strip()
        """
        :type s: str
        :rtype: str
        """
        