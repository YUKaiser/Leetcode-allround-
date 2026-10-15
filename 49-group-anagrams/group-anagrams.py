class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res=[]
        dicta={}
        for ch in strs:
            a="".join(sorted(ch))
            res.append(a)

        dicta={}
        for i in range(len(strs)):
            if res[i] not in dicta:
                dicta[res[i]]=[strs[i]]
            else:
                dicta[res[i]].append(strs[i])

        ans=[]
        for key in dicta.keys():
            ans.append(dicta[key])
        return ans