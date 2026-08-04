class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        if k==len(cardPoints):
            return sum(cardPoints)
        result=cardPoints+cardPoints
        i=len(cardPoints)-k
        j=len(cardPoints)-1
        sumi=sum(result[i:j+1])
        it=k
        maxi=sumi
        while it>0:
            sumi-=result[i]
            i+=1
            j+=1
            sumi+=result[j]
            maxi=max(maxi,sumi)
            it-=1
        return maxi