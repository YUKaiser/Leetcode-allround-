class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        maxi=0
        i=0
        dicta={}
        for j in range(len(fruits)):
            dicta[fruits[j]]=dicta.get(fruits[j],0)+1
            if len(dicta)<=2:
                maxi=max(j-i+1,maxi)
            else:
                dicta[fruits[i]]-=1
                if dicta[fruits[i]]==0:
                    del dicta[fruits[i]]
                i+=1
        return maxi        