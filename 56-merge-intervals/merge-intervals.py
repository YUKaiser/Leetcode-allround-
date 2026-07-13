class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        a=sorted(intervals)
        i=0

        while i<(len(a)-1):
            if a[i][1]>=a[i+1][0]:
                a[i]=[a[i][0],max(a[i][1],a[i+1][1])]
                a.pop(i+1)
            else:
                i+=1
        return a