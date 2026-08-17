class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x:(x[0],x[1]))
        check=intervals[0]
        cnt=0
        for i in range(1,len(intervals)):
            if check[1]>intervals[i][0]:
                if intervals[i][1]>=check[1]:
                    cnt+=1
                else:
                    cnt+=1
                    check=intervals[i]
            else:
                check=intervals[i]
        return cnt
        