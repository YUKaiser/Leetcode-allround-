class Solution(object):
    def reverseString(self, s):
        left=0
        right=len(s)-1
        while left<right:
            a=s[left]
            s[left]=s[right]
            s[right]=a
            left +=1
            right -=1
        return s

        