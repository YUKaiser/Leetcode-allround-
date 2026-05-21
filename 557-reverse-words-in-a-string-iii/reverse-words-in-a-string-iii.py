class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=s.split()
        b=" "
        for i in range(len(a)):
            a[i]=a[i][::-1]
            b=b+" "+a[i]

        return b.strip()
        