class Solution(object):
    def maxDepth(self, s):
        count=0
        re=0
        for cr in s:
            if cr=="(":
                count +=1
                re=max(re,count)
            elif cr==")":
                count =count-1

        return re

       