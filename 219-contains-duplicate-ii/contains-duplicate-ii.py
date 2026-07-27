class Solution(object):
    def containsNearbyDuplicate(self, arr, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dicta={}
        for i in range(len(arr)):
            if arr[i] in dicta:
                if abs(dicta[arr[i]]-i)<=k:
                    return True
                
            dicta[arr[i]]=i
        return False