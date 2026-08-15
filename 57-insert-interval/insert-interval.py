class Solution(object):
    def insert(self, intervals, newInterval):
        res = []

        for i in range(len(intervals)):

            # interval is completely before newInterval
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])

            # interval is completely after newInterval
            elif intervals[i][0] > newInterval[1]:
                res.append(newInterval)

                for j in range(i, len(intervals)):
                    res.append(intervals[j])

                return res

            # overlapping
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])

        # newInterval belongs at the end
        res.append(newInterval)

        return res