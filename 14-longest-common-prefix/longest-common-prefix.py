class Solution(object):
    def longestCommonPrefix(self, strs):
        initial_val=strs[0]
        for i in range(len(strs)-1):
            s1=initial_val
            s2=strs[i+1]
            prf=""
            for j in range(min(len(s1),len(s2))):
                if s1[j]==s2[j]:
                    prf=prf+s1[j]
                else:
                    break
            initial_val=prf
        return initial_val
        """
        :type strs: List[str]
        :rtype: str
        """
        