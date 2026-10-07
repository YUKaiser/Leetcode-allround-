class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dicta={'I':1,"IV":4,"V":5,"IX":9,"X":10,"XL":40,"L":50,"XC":90,"C":100,"CD":400,"D":500,"CM":900,"M":1000}
        if len(s)<2:
            return dicta[s[0]]
        key=0
        a=0
        b=1
        sumi=0
        while a<len(s):
            if b<len(s):

                if s[a]+s[b] in dicta :
                    sumi+=dicta[s[a]+s[b]]
                    a=b+1
                    b=b+2
                
                else:
                    sumi+=dicta[s[a]]
                    a=b
                    b=b+1
            else:
                sumi+=dicta[s[a]]
                a+=1   
        
        return sumi
