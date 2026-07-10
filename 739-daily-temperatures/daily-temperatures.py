class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stk=[]
        final=[]
        for i in range(len(temperatures)-1,-1,-1):
            while (stk and temperatures[i]>=temperatures[stk[-1]]):
                stk.pop()
                
            if stk:
                final.append(stk[-1]-i)
            else:
                final.append(0)
                
            stk.append(i)
        final.reverse()        
        return final                #see here if we write final.reverse()-it will return None kuki
                                    #Methods which change the list return None
