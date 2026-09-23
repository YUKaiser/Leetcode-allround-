class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        res=[0]
        sumi=0
        maxi=sumi
        for i in range(len(gain)):
            sumi+=gain[i]
            maxi=max(sumi,maxi)
            
        return maxi 
        