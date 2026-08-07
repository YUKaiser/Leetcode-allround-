class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        dicta={5:0,10:0,20:0}
        for i in range(len(bills)):
            
            if bills[i]!=5:
                if bills[i]==10:
                    if dicta[5]>0:
                        dicta[5]-=1
                    else:
                        return False
                if bills[i]==20:
                    if dicta[5]>0 and dicta[10]>0:
                        dicta[5]-=1
                        dicta[10]-=1
                    elif dicta[5]>=3:
                        dicta[5]-=3
                    else:
                        return False
            dicta[bills[i]]+=1   
        return True