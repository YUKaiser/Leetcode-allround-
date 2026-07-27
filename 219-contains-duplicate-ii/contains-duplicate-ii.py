class Solution(object):
    def containsNearbyDuplicate(self, arr, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        i=0
        seta=set()
        j=0
        while j<len(arr):
            if j-i>k:
                seta.remove(arr[i])
                i+=1
            if arr[j] in seta:
                return True
            seta.add(arr[j])
            j+=1
        return False